class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        if isinstance(other, Number):
            return self.value + other.value
        return Number(self.value + other)
    
    def __sub__(self, other):
        return Number(self.value - other.value)
    
    def __mul__(self, other):
        return Number(self.value * other.value)
    
    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("không thể chia cho 0")
        return Number(self.value / other.value)
    
    def __str__(self):
        return str(self.value)
    
a = Number(10)
b = Number(5)

print(a + b)
print(a - b)
print(a * b)
print(a / b)