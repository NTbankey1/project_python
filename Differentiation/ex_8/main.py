from abc import ABC, abstractmethod
import math

# Lớp trừu tượng
class SolidShape(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass

# Hình cầu
class Sphere(SolidShape):
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return round((4/3) * math.pi * self.radius**3, 2)

    def surface_area(self):
        return round(4 * math.pi * self.radius**2, 2)

# Hình trụ
class Cylinder(SolidShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return round(math.pi * self.radius**2 * self.height, 2)

    def surface_area(self):
        return round(2 * math.pi * self.radius * (self.radius + self.height), 2)

# Sử dụng
sphere = Sphere(3)
cylinder = Cylinder(3, 5)

print("Thể tích hình cầu:", sphere.volume())  # ✅ 113.1
print("Diện tích mặt cầu:", sphere.surface_area())  # ✅ 113.1
print("Thể tích hình trụ:", cylinder.volume())  # ✅ 141.37
print("Diện tích mặt hình trụ:", cylinder.surface_area())  # ✅ 150.8
