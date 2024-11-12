from PaymentMethod import PaymentMethod


class PayPalPayment(PaymentMethod):
    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email

    def process_payment(self):
        print(f"{self.amount} {self.currency} are being processed from {self.email}")

