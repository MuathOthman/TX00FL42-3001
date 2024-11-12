from Employee import Employee


class HourlyPaid(Employee):

    def __init__(self, first_name, last_name, hourly_pay):
        self.hourly_pay = hourly_pay
        super().__init__(first_name, last_name)

    def print_information(self):
        super().print_information()
        print(f"Your hourly pay is {self.hourly_pay}")