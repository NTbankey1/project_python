import hashlib

class  User():
    def __init__(self,username, password ):
        self.username = username
        self.password = self.__encrypt__password(password)

    def __encrypt__password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        return self.password == self.__encrypt__password(password)
    

user = User("admin", "password")
print(user.verify_password("password"))  # True
print(user.verify_password("wrong_password"))  # False