from Employee import Employee


class MonthlyPaid(Employee):

    def __init__(self, first_name, last_name, monthly_pay):
        self.monthly_pay = monthly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Your salary is {self.monthly_pay}")