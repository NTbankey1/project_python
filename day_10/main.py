import os
import time
import string

class CaesarCipher:
    def __init__(self):
        # Tạo bảng chữ cái cho tiếng Việt và tiếng Anh
        self.vietnamese_chars = string.ascii_letters + string.digits + "áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ "
        
        self.english_chars = string.ascii_letters + string.digits + string.punctuation + " "

    def encrypt(self, text, shift, language='en'):
        """Mã hóa văn bản sử dụng Caesar Cipher"""
        result = ""
        # Chọn bảng ký tự dựa trên ngôn ngữ
        chars = self.english_chars if language == 'en' else self.vietnamese_chars
        
        for char in text:
            if char in chars:
                # Tìm vị trí của ký tự trong bảng
                index = chars.find(char)
                # Dịch chuyển ký tự theo shift
                new_index = (index + shift) % len(chars)
                result += chars[new_index]
            else:
                result += char
        return result

    def decrypt(self, text, shift, language='en'):
        """Giải mã văn bản đã được mã hóa"""
        # Giải mã bằng cách dịch ngược lại
        return self.encrypt(text, -shift, language)

    def brute_force(self, text, language='en'):
        """Thử tất cả các khả năng shift có thể"""
        chars = self.english_chars if language == 'en' else self.vietnamese_chars
        results = []
        
        for shift in range(len(chars)):
            decrypted = self.decrypt(text, shift, language)
            results.append((shift, decrypted))
        return results

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cipher = CaesarCipher()
    
    while True:
        try:
            clear_screen()
            print("=== Ứng dụng Mã Hóa/Giải Mã Caesar Cipher ===")
            print("1. Mã hóa văn bản")
            print("2. Giải mã văn bản")
            print("3. Dò tìm tất cả khả năng (Brute Force)")
            print("4. Thoát")
            
            choice = input("\nNhập lựa chọn của bạn (1-4): ").strip()
            
            if choice == '4':
                break
                
            if choice in ['1', '2', '3']:
                # Chọn ngôn ngữ
                print("\nChọn ngôn ngữ:")
                print("1. Tiếng Anh")
                print("2. Tiếng Việt")
                lang_choice = input("Nhập lựa chọn (1-2): ").strip()
                language = 'en' if lang_choice == '1' else 'vi'
                
                # Nhập văn bản
                text = input("\nNhập văn bản: ").strip()
                
                if not text:
                    print("Văn bản không được để trống!")
                    time.sleep(2)
                    continue
                
                if choice in ['1', '2']:
                    # Nhập độ dịch chuyển
                    try:
                        shift = int(input("Nhập độ dịch chuyển (số nguyên): "))
                    except ValueError:
                        print("Độ dịch chuyển không hợp lệ!")
                        time.sleep(2)
                        continue
                    
                    # Thực hiện mã hóa hoặc giải mã
                    result = cipher.encrypt(text, shift, language) if choice == '1' else cipher.decrypt(text, shift, language)
                    print("\nKết quả:", result)
                    
                else:  # Brute Force
                    print("\nĐang thử tất cả các khả năng...")
                    results = cipher.brute_force(text, language)
                    print("\nKết quả Brute Force:")
                    for shift, result in results:
                        print(f"Độ dịch: {shift:2d} | Kết quả: {result}")
                
                input("\nNhấn Enter để tiếp tục...")
                
            else:
                print("Lựa chọn không hợp lệ!")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\nĐang thoát chương trình...")
            break
        except Exception as e:
            print(f"\nLỗi: {str(e)}")
            time.sleep(2)
    
    print("\nCảm ơn bạn đã sử dụng ứng dụng!")

if __name__ == "__main__":
    main() 