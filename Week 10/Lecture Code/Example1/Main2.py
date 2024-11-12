from Employee import Employee
from HourlyPaid import HourlyPaid
from MonthlyPaid import MonthlyPaid


employees = []
employees.append(HourlyPaid("Viivi", "Virta", 12.35))
employees.append(MonthlyPaid("Ahmed", "Habib", 2750))
employees.append(Employee("Pekka", "Puro"))
employees.append(HourlyPaid("Olga", "Glebova", 14.92))

for employee in employees:
    employee.print_information()