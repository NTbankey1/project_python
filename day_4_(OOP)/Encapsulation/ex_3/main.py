class Parent:
    def __init__ (self):
        self.__secret = "This is private"

    def get_secret (self):
        return self.__secret
    

class Child(Parent):
    def reveal_secret (self):
        return self.__secret
 
p = Parent()
print(p.get_secret())
print(p._Parent__secret)