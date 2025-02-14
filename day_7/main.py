from collections import Counter
import re
import string
from typing import Dict, List, Tuple, Union
import matplotlib.pyplot as plt
from pathlib import Path
import json

class TextAnalyzer:
    """Class phân tích văn bản với nhiều tính năng nâng cao."""
    
    def __init__(self):
        """Khởi tạo TextAnalyzer với các thuộc tính cần thiết."""
        self.__text = ""
        self.__words = []
        self.__chars = []
        self.__word_freq = Counter()
        self.__char_freq = Counter()
        self.__ngram_freq = {}
        self.__stop_words = set()
        
    def load_text_from_file(self, file_path: str) -> bool:
        """Đọc văn bản từ file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.__text = file.read()
            self.__preprocess_text()
            return True
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")
            return False
    
    def set_text(self, text: str) -> None:
        """Thiết lập văn bản trực tiếp."""
        self.__text = text
        self.__preprocess_text()
    
    def load_stop_words(self, file_path: str) -> bool:
        """Nạp danh sách stop words từ file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                self.__stop_words = set(file.read().splitlines())
            return True
        except Exception as e:
            print(f"Lỗi khi đọc file stop words: {e}")
            return False
    
    def __preprocess_text(self) -> None:
        """Tiền xử lý văn bản."""
        # Chuyển về chữ thường
        text = self.__text.lower()
        
        # Tách từ
        self.__words = re.findall(r'\b\w+\b', text)
        
        # Tách ký tự (loại bỏ khoảng trắng và dấu câu)
        self.__chars = [c for c in text if c not in string.whitespace + string.punctuation]
        
        # Tính tần suất
        self.__calculate_frequencies()
    
    def __calculate_frequencies(self) -> None:
        """Tính toán tần suất của từ và ký tự."""
        # Tần suất từ (loại bỏ stop words nếu có)
        words = [w for w in self.__words if w not in self.__stop_words]
        self.__word_freq = Counter(words)
        
        # Tần suất ký tự
        self.__char_freq = Counter(self.__chars)
    
    def analyze_ngrams(self, n: int) -> Dict[str, int]:
        """Phân tích n-gram của văn bản."""
        if n < 1:
            raise ValueError("n phải lớn hơn 0")
            
        ngrams = []
        for i in range(len(self.__words) - n + 1):
            ngram = ' '.join(self.__words[i:i+n])
            ngrams.append(ngram)
        
        self.__ngram_freq[n] = Counter(ngrams)
        return dict(self.__ngram_freq[n])
    
    def get_word_frequency(self, top_n: int = None) -> List[Tuple[str, int]]:
        """Lấy tần suất xuất hiện của từ."""
        return self.__word_freq.most_common(top_n)
    
    def get_char_frequency(self, top_n: int = None) -> List[Tuple[str, int]]:
        """Lấy tần suất xuất hiện của ký tự."""
        return self.__char_freq.most_common(top_n)
    
    def get_ngram_frequency(self, n: int, top_n: int = None) -> List[Tuple[str, int]]:
        """Lấy tần suất xuất hiện của n-gram."""
        if n not in self.__ngram_freq:
            self.analyze_ngrams(n)
        return self.__ngram_freq[n].most_common(top_n)
    
    def plot_frequency(self, freq_type: str = 'word', top_n: int = 10) -> None:
        """Vẽ biểu đồ tần suất."""
        if freq_type == 'word':
            data = self.get_word_frequency(top_n)
            title = f'Top {top_n} từ xuất hiện nhiều nhất'
        elif freq_type == 'char':
            data = self.get_char_frequency(top_n)
            title = f'Top {top_n} ký tự xuất hiện nhiều nhất'
        else:
            raise ValueError("freq_type phải là 'word' hoặc 'char'")
        
        labels, values = zip(*data)
        plt.figure(figsize=(12, 6))
        plt.bar(labels, values)
        plt.title(title)
        plt.xticks(rotation=45)
        plt.xlabel('Từ/Ký tự')
        plt.ylabel('Tần suất')
        plt.tight_layout()
        plt.show()
    
    def export_results(self, file_path: str, include_ngrams: bool = False) -> bool:
        """Xuất kết quả phân tích ra file JSON."""
        try:
            results = {
                'word_frequency': dict(self.__word_freq),
                'char_frequency': dict(self.__char_freq)
            }
            
            if include_ngrams and self.__ngram_freq:
                results['ngram_frequency'] = {
                    f'{n}-gram': dict(freq)
                    for n, freq in self.__ngram_freq.items()
                }
            
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(results, file, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Lỗi khi xuất kết quả: {e}")
            return False

def main():
    """Hàm chính để demo ứng dụng."""
    analyzer = TextAnalyzer()
    
    # Demo với văn bản mẫu
    sample_text = """
    Python là một ngôn ngữ lập trình bậc cao, dễ đọc và dễ học.
    Python hỗ trợ nhiều mô hình lập trình, bao gồm lập trình hướng đối tượng.
    Python được sử dụng rộng rãi trong khoa học dữ liệu và trí tuệ nhân tạo.
    """
    
    print("=== Demo phân tích tần suất văn bản ===")
    
    # Thiết lập văn bản
    analyzer.set_text(sample_text)
    
    # Phân tích và hiển thị kết quả
    print("\n1. Tần suất xuất hiện của từ:")
    word_freq = analyzer.get_word_frequency(top_n=5)
    for word, freq in word_freq:
        print(f"  {word}: {freq} lần")
    
    print("\n2. Tần suất xuất hiện của ký tự:")
    char_freq = analyzer.get_char_frequency(top_n=5)
    for char, freq in char_freq:
        print(f"  {char}: {freq} lần")
    
    print("\n3. Phân tích 2-gram:")
    bigrams = analyzer.analyze_ngrams(2)
    for bigram, freq in list(bigrams.items())[:5]:
        print(f"  {bigram}: {freq} lần")
    
    # Vẽ biểu đồ
    print("\n4. Vẽ biểu đồ tần suất từ")
    analyzer.plot_frequency(freq_type='word', top_n=10)
    
    print("\n5. Vẽ biểu đồ tần suất ký tự")
    analyzer.plot_frequency(freq_type='char', top_n=10)
    
    # Xuất kết quả
    print("\n6. Xuất kết quả ra file JSON")
    if analyzer.export_results('text_analysis_results.json', include_ngrams=True):
        print("  Đã xuất kết quả thành công!")
    else:
        print("  Xuất kết quả thất bại!")

if __name__ == "__main__":
    main() 