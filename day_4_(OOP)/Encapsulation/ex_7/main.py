class SecureMeta(type):
    def __new__(cls, name, bases, dct):
        for attr in dct:
            if attr.startswith("__") and attr.endswith("__"):
                continue
            if attr.startswith("__"):
                raise AttributeError(f"Protected/private attributes ('{attr}) not allowed in metaclass")
        return super().__new__(cls, name, bases, dct)

class SecureClass(metaclass=SecureMeta):
    def __init__(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data
    

obj = SecureClass("Sensitive Data")
print(obj.get_data())
