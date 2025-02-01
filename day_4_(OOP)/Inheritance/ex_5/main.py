from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "meow!"

dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())