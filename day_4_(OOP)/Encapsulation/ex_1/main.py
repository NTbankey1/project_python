class BankAccount:
    def __init__(self, account_number, balance, amount):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute
        self.__amount = amount # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        if amount > self.__balance:
            return "Insufficient balance"
        self.__balance -= amount
        return f"Withdrew {amount}. New balance: {self.__balance}"

    def get_balance(self):
        return f"Current balance: {self.__balance}"

# Sử dụng
account = BankAccount("123456", 1000, 1000)
print(account.deposit(500))  # ✅ Deposited 500. New balance: 1500
print(account.withdraw(300))  # ✅ Withdrew 300. New balance: 1200
print(account.get_balance())  # ✅ Current balance: 1200
