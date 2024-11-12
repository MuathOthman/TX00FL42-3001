from Employee import Employee


employees = []
employees.append(Employee("Viivi", "Virta"))
employees.append(Employee("Ahmed", "Habib"))

for e in employees:
    e.print_information()