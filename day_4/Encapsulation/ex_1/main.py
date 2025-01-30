class Bankaccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number 
        self._balance = balance 
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount 
            return f"Deposited {amount}. New balance: {self._balance}"
        return "invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"withdrew {amount} to {self._balance}"
        return "Invalid withdrawal amount or insufficient amount"
    
    def get_balance(self):
        return f"current balance: {self._balance}"
    
account = Bankaccount("123456", 1000)
print(account.deposit(500))
print(account.withdraw(300))
print(account.get_balance())