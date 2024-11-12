from PaymentMethod import PaymentMethod


class CreditCardPayment(PaymentMethod):
    def __init__(self, amount, currency, card_num, exp):
        super().__init__(amount, currency)
        self.card_num = card_num
        self.exp = exp

    def process_payment(self):
        print(f"{self.amount} {self.currency} are being processed from {self.card_num[-4:]}")
