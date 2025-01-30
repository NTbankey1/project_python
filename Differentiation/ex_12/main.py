from abc import ABC, abstractmethod

# Lớp trừu tượng
class ModularArithmetic(ABC):
    def __init__(self, modulus):
        self.modulus = modulus

    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

# Số học mô-đun
class Modulo(ModularArithmetic):
    def add(self, a, b):
        return (a + b) % self.modulus

    def multiply(self, a, b):
        return (a * b) % self.modulus

# Sử dụng
mod7 = Modulo(7)

print("5 + 3 mod 7 =", mod7.add(5, 3))  # ✅ 1
print("4 * 6 mod 7 =", mod7.multiply(4, 6))  # ✅ 3
