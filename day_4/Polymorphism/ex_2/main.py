class Animal:
    def speak(self):
        return "Animal make a sound"
    
class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow!"

animals = [Animal(),Dog(), Cat()]
for animal in animals:
    print(animal.speak())