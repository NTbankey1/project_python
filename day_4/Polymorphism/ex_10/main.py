class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Sử dụng
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, -4)

print("Cộng:", c1 + c2)  # ✅ 3 - 1i
print("Nhân:", c1 * c2)  # ✅ 14 + 5i
