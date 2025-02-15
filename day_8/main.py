from collections import Counter
from spellchecker import SpellChecker
import string

def analyze_text(text):
    # Khởi tạo spell checker
    spell = SpellChecker(language='en')
    
    # Phân tích tần suất chữ cái
    def analyze_characters(text):
        # Loại bỏ khoảng trắng và chuyển về chữ thường
        text = text.lower()
        # Đếm tần suất các chữ cái
        char_count = Counter(c for c in text if c.isalpha())
        return char_count
    
    # Phân tích tần suất từ
    def analyze_words(text):
        # Chuyển về chữ thường và tách thành các từ
        words = text.lower().split()
        # Loại bỏ dấu câu từ mỗi từ
        words = [''.join(c for c in word if c not in string.punctuation) for word in words]
        # Đếm tần suất các từ
        word_count = Counter(words)
        return word_count
    
    # Kiểm tra chính tả
    def check_spelling(words):
        # Tìm các từ viết sai
        misspelled = spell.unknown(words)
        corrections = {}
        for word in misspelled:
            # Lấy các gợi ý sửa lỗi cho từng từ
            corrections[word] = spell.candidates(word)
        return corrections

    # Thực hiện phân tích
    char_frequency = analyze_characters(text)
    word_frequency = analyze_words(text)
    words = [word.strip(string.punctuation) for word in text.lower().split()]
    spelling_corrections = check_spelling(words)

    return char_frequency, word_frequency, spelling_corrections

def main():
    print("Chọn cách nhập văn bản:")
    print("1. Nhập trực tiếp")
    print("2. Đọc từ file")
    
    choice = input("Lựa chọn của bạn (1/2): ")
    
    if choice == "1":
        text = input("Nhập văn bản của bạn: ")
    elif choice == "2":
        file_path = input("Nhập đường dẫn đến file: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print("Không tìm thấy file!")
            return
    else:
        print("Lựa chọn không hợp lệ!")
        return

    # Phân tích văn bản
    char_freq, word_freq, spelling_corrections = analyze_text(text)

    # Hiển thị kết quả
    print("\n=== Tần suất xuất hiện của chữ cái ===")
    for char, count in sorted(char_freq.items()):
        print(f"'{char}': {count} lần")

    print("\n=== Tần suất xuất hiện của từ ===")
    for word, count in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        if word:  # Chỉ in những từ không rỗng
            print(f"'{word}': {count} lần")

    if spelling_corrections:
        print("\n=== Các từ có thể bị sai chính tả ===")
        for word, suggestions in spelling_corrections.items():
            print(f"'{word}' - Gợi ý sửa: {', '.join(suggestions)}")

if __name__ == "__main__":
    main()