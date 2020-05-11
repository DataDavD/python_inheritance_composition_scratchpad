import json

from hr import calculate_payroll
from productivity import track
from employees import employee_database, Employee


def print_dict(d):
    print(json.dumps(d, indent=2))


employees = employee_database.employees

track(employees, 40)
calculate_payroll(employees)

temp_secretary = Employee(5)
print('Temporary Secretary:')
print_dict(temp_secretary.to_dict())

employee_4 = Employee(4)
print('Employee with ID 4:')
print_dict(employee_4.to_dict())
