from abc import ABC, abstractmethod
import math

# Lớp trừu tượng
class CoordinateSystem(ABC):
    @abstractmethod
    def convert_to_cartesian(self):
        pass

    @abstractmethod
    def convert_to_polar(self):
        pass

# Hệ tọa độ Descartes (x, y)
class CartesianCoordinate(CoordinateSystem):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def convert_to_cartesian(self):
        return (self.x, self.y)

    def convert_to_polar(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return (round(r, 2), round(math.degrees(theta), 2))

# Hệ tọa độ cực (r, θ)
class PolarCoordinate(CoordinateSystem):
    def __init__(self, r, theta):
        self.r = r
        self.theta = math.radians(theta)  # Chuyển về radian

    def convert_to_cartesian(self):
        x = self.r * math.cos(self.theta)
        y = self.r * math.sin(self.theta)
        return (round(x, 2), round(y, 2))

    def convert_to_polar(self):
        return (self.r, round(math.degrees(self.theta), 2))

# Sử dụng
cartesian = CartesianCoordinate(3, 4)
polar = PolarCoordinate(5, 53)

print("Cartesian -> Polar:", cartesian.convert_to_polar())  # ✅ (5.0, 53.13)
print("Polar -> Cartesian:", polar.convert_to_cartesian())  # ✅ (3.0, 4.0)
