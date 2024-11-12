class PaymentMethod:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def process_payment(self):
        print(f"{self.amount} {self.currency} are being processed")