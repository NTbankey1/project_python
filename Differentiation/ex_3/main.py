from abc import ABC, abstractmethod

# Lớp trừu tượng
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"Thanh toán {amount} bằng thẻ tín dụng {self.card_number}"

class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Thanh toán {amount} bằng PayPal ({self.email})"

class BitcoinPayment(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Thanh toán {amount} bằng Bitcoin ({self.wallet_address})"

# Sử dụng
payment1 = CreditCardPayment("1234-5678-9012")
payment2 = PayPalPayment("user@example.com")
payment3 = BitcoinPayment("3FZbgi29...")

print(payment1.pay(100))  # ✅ Thanh toán 100 bằng thẻ tín dụng 1234-5678-9012
print(payment2.pay(200))  # ✅ Thanh toán 200 bằng PayPal (user@example.com)
print(payment3.pay(300))  # ✅ Thanh toán 300 bằng Bitcoin (3FZbgi29...)
