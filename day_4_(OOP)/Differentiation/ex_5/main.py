from abc import ABC, abstractmethod

# Lớp trừu tượng
class ArithmeticOperation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

# Cộng
class Addition(ArithmeticOperation):
    def calculate(self, a, b):
        return a + b

# Trừ
class Subtraction(ArithmeticOperation):
    def calculate(self, a, b):
        return a - b

# Nhân
class Multiplication(ArithmeticOperation):
    def calculate(self, a, b):
        return a * b

# Chia
class Division(ArithmeticOperation):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Không thể chia cho 0")
        return a / b

# Sử dụng
operations = [Addition(), Subtraction(), Multiplication(), Division()]

a, b = 10, 5
for op in operations:
    print(f"{op.__class__.__name__}: {op.calculate(a, b)}")

# ✅ Output:
# Addition: 15
# Subtraction: 5
# Multiplication: 50
# Division: 2.0
