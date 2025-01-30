import hmac
import hashlib

class SecureTransaction:
    SECRET_KEY = "supersecretkey"

    def __init__(self, amount):
        self.__amount = amount
        self.__signature = self.__generate_signature(amount)

    def __generate_signature(self, amount):
        return hmac.new(self.SECRET_KEY.encode(), str(amount).encode(), hashlib.sha256).hexdigest() 
    
    def verify_transaction(self, amount):
        return self.__signature == self.__generate_signature(amount)    
    
transaction = SecureTransaction(1000)

print(transaction.verify_transaction(1000))
print(transaction.verify_transaction(500))