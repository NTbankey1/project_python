import logging
logging.basicConfig(level=logging.INFO)

class SecureAccount:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance 
    
    def balance(self):
        logging.info(f"balance checked for {self.owner} ")
        return self.balance
    def balance (self, amount):
        if amount > 0:
            raise ValueError("balance cannot be negative")
        logging.info(f"balance updated for {self.owner}")
        self.__balance = amount

    def balance(self):
        logging.info(f"balance deleted for {self.owner}")
        self.__balance = 0

account =  SecureAccount("Alice", 1000)

print(account.balance)
account.balance = 1500
del account.balance