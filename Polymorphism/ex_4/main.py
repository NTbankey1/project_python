from abc import ABC, abstractmethod

class Shape(ABC):
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 *(self.radius)**2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        def area(self):
            return self.width * self.height
        
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())