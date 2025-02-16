from gtts import gTTS
import pygame
import os
import time
from threading import Thread, Lock
from queue import Queue
import re
import hashlib
import json
from tqdm import tqdm
import concurrent.futures
import tempfile
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import sys

class TextToSpeechConverter:
    def __init__(self):
        self.cache_dir = "speech_cache"
        self.temp_dir = tempfile.mkdtemp()
        self.cache_file = os.path.join(self.cache_dir, "cache_index.json")
        self.lock = Lock()
        self.failed_chunks = []
        self.setup_cache()
        self.setup_session()
        
    def setup_session(self):
        """Thiết lập session với retry tự động"""
        self.session = requests.Session()
        retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504]
        )
        self.session.mount('http://', HTTPAdapter(max_retries=retries))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def setup_cache(self):
        """Khởi tạo thư mục cache"""
        try:
            if not os.path.exists(self.cache_dir):
                os.makedirs(self.cache_dir)
            if not os.path.exists(self.cache_file):
                with open(self.cache_file, 'w', encoding='utf-8') as f:
                    json.dump({}, f)
        except Exception as e:
            print(f"Lỗi khi tạo cache: {str(e)}")
            self.cache_dir = tempfile.mkdtemp()
            self.cache_file = os.path.join(self.cache_dir, "cache_index.json")

    def process_chunk_with_retry(self, text, language, max_retries=3):
        """Xử lý chunk với khả năng thử lại"""
        for attempt in range(max_retries):
            try:
                tts = gTTS(text=text, lang=language, slow=False)
                temp_file = os.path.join(self.temp_dir, f"temp_{hashlib.md5(text.encode()).hexdigest()}.mp3")
                tts.save(temp_file)
                return temp_file
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"\nLỗi sau {max_retries} lần thử với đoạn: {text[:50]}...")
                    print(f"Chi tiết lỗi: {str(e)}")
                    return None
                time.sleep(1)  # Đợi 1 giây trước khi thử lại
        return None

    def process_chunk(self, text, language):
        """Xử lý từng đoạn văn bản với cache"""
        if not text.strip():
            return None
            
        cache_key = self.get_cache_key(text, language)
        cached_path = self.get_from_cache(cache_key)
        
        if cached_path:
            return cached_path
            
        try:
            temp_file = self.process_chunk_with_retry(text, language)
            if temp_file:
                return self.save_to_cache(cache_key, temp_file)
            return None
        except Exception as e:
            print(f"\nLỗi khi xử lý đoạn: {str(e)}")
            return None

    def convert_and_play(self):
        """Hàm chính để chuyển đổi và phát âm thanh"""
        try:
            print("\nNhập văn bản (nhấn Enter hai lần để kết thúc):")
            lines = []
            while True:
                try:
                    line = input()
                    if line:
                        lines.append(line)
                    else:
                        break
                except KeyboardInterrupt:
                    print("\nĐã hủy nhập văn bản.")
                    return
                except EOFError:
                    break

            text = ' '.join(lines)
            if not text.strip():
                print("Văn bản không được để trống!")
                return

            language = input("Nhập ngôn ngữ (vi/en): ").strip().lower()
            if language not in ['vi', 'en']:
                print("Ngôn ngữ không hợp lệ! Sử dụng tiếng Việt (vi)")
                language = 'vi'

            chunks = self.split_text(text)
            total_chunks = len(chunks)
            print(f"\nTổng số đoạn cần xử lý: {total_chunks}")

            # Xử lý từng chunk với progress bar
            audio_files = []
            failed_chunks = []
            
            with tqdm(total=total_chunks, desc="Đang xử lý") as pbar:
                for i, chunk in enumerate(chunks):
                    try:
                        audio_file = self.process_chunk(chunk, language)
                        if audio_file:
                            audio_files.append((i, audio_file))
                        else:
                            failed_chunks.append((i, chunk))
                        pbar.update(1)
                    except Exception as e:
                        print(f"\nLỗi khi xử lý đoạn {i+1}: {str(e)}")
                        failed_chunks.append((i, chunk))
                        pbar.update(1)

            # Thử lại các chunk bị lỗi
            if failed_chunks:
                print(f"\nĐang thử lại {len(failed_chunks)} đoạn bị lỗi...")
                for i, chunk in failed_chunks:
                    try:
                        audio_file = self.process_chunk_with_retry(chunk, language, max_retries=5)
                        if audio_file:
                            audio_files.append((i, audio_file))
                    except Exception as e:
                        print(f"Không thể xử lý đoạn {i+1}: {str(e)}")

            # Phát âm thanh theo thứ tự
            if audio_files:
                print("\nĐang phát âm thanh...")
                for _, audio_file in sorted(audio_files):
                    self.play_audio(audio_file)
            else:
                print("Không có đoạn âm thanh nào được tạo thành công!")

        except KeyboardInterrupt:
            print("\nĐã hủy quá trình xử lý.")
        except Exception as e:
            print(f"Lỗi không mong muốn: {str(e)}")
        finally:
            self.cleanup()

    def cleanup(self):
        """Dọn dẹp tài nguyên"""
        try:
            pygame.mixer.quit()
            for file in os.listdir(self.temp_dir):
                try:
                    os.remove(os.path.join(self.temp_dir, file))
                except:
                    pass
            try:
                os.rmdir(self.temp_dir)
            except:
                pass
        except:
            pass

    def get_cache_key(self, text, language):
        """Tạo key cho cache"""
        return hashlib.md5(f"{text}:{language}".encode()).hexdigest()

    def get_from_cache(self, cache_key):
        """Lấy audio từ cache"""
        try:
            with self.lock:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    cache = json.load(f)
                if cache_key in cache:
                    cache_path = os.path.join(self.cache_dir, f"{cache_key}.mp3")
                    if os.path.exists(cache_path):
                        return cache_path
        except Exception as e:
            print(f"Lỗi khi đọc cache: {str(e)}")
        return None

    def save_to_cache(self, cache_key, audio_path):
        """Lưu audio vào cache"""
        try:
            with self.lock:
                with open(self.cache_file, 'r', encoding='utf-8') as f:
                    cache = json.load(f)
                cache[cache_key] = True
                with open(self.cache_file, 'w', encoding='utf-8') as f:
                    json.dump(cache, f)
                
                cache_path = os.path.join(self.cache_dir, f"{cache_key}.mp3")
                if os.path.exists(audio_path):
                    os.rename(audio_path, cache_path)
                return cache_path
        except Exception as e:
            print(f"Lỗi khi lưu cache: {str(e)}")
            return audio_path

    def split_text(self, text, max_length=500):
        """Chia văn bản thành các đoạn nhỏ hơn"""
        if not text:
            return []
        
        sentences = re.split('([.!?]+[\s\n]*)', text)
        chunks = []
        current_chunk = ""
        
        for i in range(0, len(sentences)-1, 2):
            sentence = sentences[i] + (sentences[i+1] if i+1 < len(sentences) else '')
            if len(current_chunk) + len(sentence) < max_length:
                current_chunk += sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        return [c for c in chunks if c.strip()]

    def play_audio(self, filename):
        """Phát file âm thanh"""
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        except Exception as e:
            print(f"Lỗi khi phát âm thanh: {str(e)}")
        finally:
            try:
                pygame.mixer.quit()
            except:
                pass

def main():
    print("Chương trình chuyển văn bản thành giọng nói")
    print("-------------------------------------------")
    print("Nhấn Ctrl+C để thoát chương trình bất cứ lúc nào")
    
    converter = TextToSpeechConverter()
    
    while True:
        try:
            # Xóa màn hình để giao diện sạch sẽ hơn
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("Chương trình chuyển văn bản thành giọng nói")
            print("-------------------------------------------")
            print("Nhấn Ctrl+C để thoát chương trình")
            print("\nLựa chọn:")
            print("1. Chuyển văn bản thành giọng nói")
            print("2. Thoát chương trình")
            
            choice = input("\nNhập lựa chọn của bạn (1-2): ").strip()
            
            if choice == '1':
                converter.convert_and_play()
            elif choice == '2':
                break
            else:
                print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")
                time.sleep(1)
                continue
                
        except KeyboardInterrupt:
            print("\n\nĐang thoát chương trình...")
            break
        except Exception as e:
            print(f"\nLỗi không mong muốn: {str(e)}")
            print("Chương trình sẽ tự động khởi động lại sau 3 giây...")
            time.sleep(3)
            continue
    
    try:
        converter.cleanup()
    except:
        pass
        
    print("\nCảm ơn bạn đã sử dụng chương trình!")
    sys.exit(0)

if __name__ == "__main__":
    main()