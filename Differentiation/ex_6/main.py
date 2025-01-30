from abc import ABC, abstractmethod
import math

# Lớp trừu tượng
class Equation(ABC):
    @abstractmethod
    def solve(self):
        pass

# Phương trình bậc 1: ax + b = 0
class LinearEquation(Equation):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve(self):
        if self.a == 0:
            return "Phương trình vô nghiệm" if self.b != 0 else "Vô số nghiệm"
        return f"Nghiệm: x = {-self.b / self.a}"

# Phương trình bậc 2: ax² + bx + c = 0
class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        if self.a == 0:
            return LinearEquation(self.b, self.c).solve()  # Nếu a = 0 thì giải như phương trình bậc 1
        delta = self.b**2 - 4*self.a*self.c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            return f"Nghiệm kép: x = {-self.b / (2*self.a)}"
        else:
            x1 = (-self.b + math.sqrt(delta)) / (2*self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2*self.a)
            return f"Nghiệm: x1 = {x1}, x2 = {x2}"

# Sử dụng
eq1 = LinearEquation(2, -4)
eq2 = QuadraticEquation(1, -3, 2)

print(eq1.solve())  # ✅ Nghiệm: x = 2.0
print(eq2.solve())  # ✅ Nghiệm: x1 = 2.0, x2 = 1.0
