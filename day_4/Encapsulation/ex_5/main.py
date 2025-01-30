import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def __encrypt__password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def verify_password(self, password):
        return self.__encrypt__password(password) == self.__encrypt__password
    
user = User("alice", "mypassword")

print(user.verify_password("mypassword"))
print(user.verify_password("wrongpassword"))