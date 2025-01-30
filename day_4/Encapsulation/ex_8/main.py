class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance 
    
    def __init__(self, data):
        self.data = data

obj1 = Singleton("First Instance")
obj2 = Singleton("Second Instance")

print(obj1.data)
print(obj2.data)

print(obj1 is obj2)