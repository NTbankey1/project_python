import logging
logging.basicConfig(level=logging.INFO)

class SecureAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Định nghĩa thuộc tính private __balance
    
    # Getter cho balance
    @property
    def balance(self):
        logging.info(f"Balance checked for {self.owner}")
        return self.__balance
    
    # Setter cho balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        logging.info(f"Balance updated for {self.owner}")
        self.__balance = amount

    # Deleter cho balance
    @balance.deleter
    def balance(self):
        logging.info(f"Balance deleted for {self.owner}")
        self.__balance = 0

# Tạo đối tượng SecureAccount
account = SecureAccount("Alice", 1000)

# Kiểm tra balance
print(account.balance)

# Cập nhật balance
account.balance = 1500

# Xoá balance
del account.balance
