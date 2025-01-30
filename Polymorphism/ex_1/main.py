class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

def make_sound(animal):
    return animal.speak()

animal = [Dog(), Cat(),Duck()]
for animal in animal:
    print(make_sound(animal))