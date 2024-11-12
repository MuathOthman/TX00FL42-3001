from PaymentMethod import PaymentMethod
from CreditCardPayment import CreditCardPayment
from PayPalPayment import PayPalPayment

method1 = PaymentMethod(20, "€")
method2 = CreditCardPayment(40, "$", "1234 4567 4532 6543", 2025)
method3 = PayPalPayment(50, "€", "muatho@gmail.com")

method2.process_payment()
method3.process_payment()