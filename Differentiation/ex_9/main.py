from abc import ABC, abstractmethod

# Lớp trừu tượng cho dãy số
class Sequence(ABC):
    @abstractmethod
    def generate(self, n):
        pass

# Dãy Fibonacci
class FibonacciSequence(Sequence):
    def generate(self, n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]

# Cấp số cộng: a_n = a1 + (n-1) * d
class ArithmeticSequence(Sequence):
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d

    def generate(self, n):
        return [self.a1 + i * self.d for i in range(n)]

# Cấp số nhân: a_n = a1 * r^(n-1)
class GeometricSequence(Sequence):
    def __init__(self, a1, r):
        self.a1 = a1
        self.r = r

    def generate(self, n):
        return [self.a1 * (self.r ** i) for i in range(n)]

# Sử dụng
fib = FibonacciSequence()
arith = ArithmeticSequence(2, 3)
geo = GeometricSequence(2, 2)

print("Fibonacci:", fib.generate(10))  # ✅ [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("Cấp số cộng:", arith.generate(10))  # ✅ [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
print("Cấp số nhân:", geo.generate(10))  # ✅ [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
