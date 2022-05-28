from Employee import Employee


class Office:

    def __init__(self, office_name):
        self.office_name = office_name
        self.employees = []

    def get_employee(self, emp_id):
        employee = list(filter(lambda emp: emp.id == emp_id, self.employees))
        if len(employee) == 0:
            return None
        return employee[0]

    def fire(self, emp_id):
        self.employees.remove(self.get_employee(emp_id))

    def hire(self, new_employee):
        self.employees.append(new_employee)


alexandria_office = Office('alexandria')

emp1 = Employee('abdullah', 2000, 'happy', 40, 10, 'abdallah@gmail.com', 10, 2000, True)
alexandria_office.hire(emp1)

print(alexandria_office.employees)
