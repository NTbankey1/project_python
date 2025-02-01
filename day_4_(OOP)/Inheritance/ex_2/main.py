class A:
    def show(self):
        return "class A"
    
class B:
    def display(self):
        return "class B"

class C(A, B):
    pass

c = C()
print(c.show())
print(c.display())