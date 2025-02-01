class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    
double = Multiplier(2)
triple = Multiplier(3)

print(double(5))
print(triple(5))