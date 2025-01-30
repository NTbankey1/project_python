class A:
    def show(self):
        return "class A"
    
class B:
    def show(self):
        return "class B"

class C(A):
    def show(self):
        return "class C"
    
class D(B, C):
    pass

d = D()
print(d.show()) 
print(D.mro())