from abc import ABC, abstractmethod

# Lớp trừu tượng
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Lớp con kế thừa từ Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Sử dụng
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Diện tích hình tròn:", circle.area())  # ✅ 78.5
print("Chu vi hình tròn:", circle.perimeter())  # ✅ 31.4

print("Diện tích hình chữ nhật:", rectangle.area())  # ✅ 24
print("Chu vi hình chữ nhật:", rectangle.perimeter())  # ✅ 20
