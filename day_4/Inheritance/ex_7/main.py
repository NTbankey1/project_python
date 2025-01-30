class Parent:
    def __init__(self):
        self.__private_var = "Secret"

    def __private_method(self):
        return "This is a private"

class Child(Parent):
    def access_private(self):
        return self._Parent__private_var
    
parent = Parent()
child = Child()

print(child.access_private())