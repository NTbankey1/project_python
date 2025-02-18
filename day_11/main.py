import os
import math
import time

class Calculator:
    def __init__(self):
        self.history = []  # Lưu lịch sử tính toán
        
    def add(self, x, y):
        return x + y
        
    def subtract(self, x, y):
        return x - y
        
    def multiply(self, x, y):
        return x * y
        
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Không thể chia cho 0!")
        return x / y
    
    def power(self, x, y):
        return math.pow(x, y)
        
    def square_root(self, x):
        if x < 0:
            raise ValueError("Không thể tính căn bậc 2 của số âm!")
        return math.sqrt(x)
        
    def save_history(self, operation, result):
        """Lưu lịch sử tính toán"""
        self.history.append((operation, result))
        if len(self.history) > 10:  # Chỉ giữ 10 phép tính gần nhất
            self.history.pop(0)

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number_input(prompt):
    """Hàm nhập số an toàn"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

def main():
    calc = Calculator()
    
    while True:
        try:
            clear_screen()
            print("=== Máy Tính Đơn Giản ===")
            print("1. Cộng")
            print("2. Trừ")
            print("3. Nhân")
            print("4. Chia")
            print("5. Lũy thừa")
            print("6. Căn bậc 2")
            print("7. Xem lịch sử")
            print("8. Thoát")
            
            choice = input("\nNhập lựa chọn của bạn (1-8): ").strip()
            
            if choice == '8':
                break
                
            if choice == '7':
                print("\n=== Lịch sử tính toán ===")
                if not calc.history:
                    print("Chưa có phép tính nào!")
                else:
                    for op, res in calc.history:
                        print(f"{op} = {res}")
                input("\nNhấn Enter để tiếp tục...")
                continue
                
            if choice in ['1', '2', '3', '4', '5']:
                x = get_number_input("Nhập số thứ nhất: ")
                y = get_number_input("Nhập số thứ hai: ")
                
                if choice == '1':
                    result = calc.add(x, y)
                    operation = f"{x} + {y}"
                elif choice == '2':
                    result = calc.subtract(x, y)
                    operation = f"{x} - {y}"
                elif choice == '3':
                    result = calc.multiply(x, y)
                    operation = f"{x} × {y}"
                elif choice == '4':
                    try:
                        result = calc.divide(x, y)
                        operation = f"{x} ÷ {y}"
                    except ValueError as e:
                        print(f"\nLỗi: {str(e)}")
                        time.sleep(2)
                        continue
                else:  # Lũy thừa
                    result = calc.power(x, y)
                    operation = f"{x} ^ {y}"
                    
            elif choice == '6':
                x = get_number_input("Nhập số cần tính căn bậc 2: ")
                try:
                    result = calc.square_root(x)
                    operation = f"√{x}"
                except ValueError as e:
                    print(f"\nLỗi: {str(e)}")
                    time.sleep(2)
                    continue
            else:
                print("Lựa chọn không hợp lệ!")
                time.sleep(1)
                continue
            
            # Hiển thị và lưu kết quả
            print(f"\nKết quả: {operation} = {result}")
            calc.save_history(operation, result)
            input("\nNhấn Enter để tiếp tục...")
            
        except KeyboardInterrupt:
            print("\nĐang thoát chương trình...")
            break
        except Exception as e:
            print(f"\nLỗi: {str(e)}")
            time.sleep(2)
    
    print("\nCảm ơn bạn đã sử dụng máy tính!")

if __name__ == "__main__":
    main() 