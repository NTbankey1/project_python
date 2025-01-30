from abc import ABC, abstractmethod
import numpy as np

# Lớp trừu tượng cho đa thức
class Polynomial(ABC):
    @abstractmethod
    def evaluate(self, x):
        pass

    @abstractmethod
    def derivative(self):
        pass

# Đa thức P(x) = a_n*x^n + ... + a_1*x + a_0
class GeneralPolynomial(Polynomial):
    def __init__(self, coefficients):
        self.coefficients = np.array(coefficients)

    def evaluate(self, x):
        return np.polyval(self.coefficients, x)

    def derivative(self):
        derived_coeffs = np.polyder(self.coefficients)
        return GeneralPolynomial(derived_coeffs)

    def __str__(self):
        return " + ".join(f"{coef}x^{i}" for i, coef in enumerate(reversed(self.coefficients)))

# Sử dụng
p = GeneralPolynomial([1, -3, 2])  # P(x) = x² - 3x + 2
print("Đa thức P(x):", p)

print("P(2) =", p.evaluate(2))  # ✅ 0
print("Đạo hàm của P(x):", p.derivative())  # ✅ 2x - 3
