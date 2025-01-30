class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance\
        
class Config(Singleton):
    def __init__(self, setting):
        if not hasattr(self, "setting"):
            self.setting = setting

config1 =Config("Dark mode")
config2 = Config("light mode")

print(config1.setting)
print(config2.setting)
print(config1 is config2)