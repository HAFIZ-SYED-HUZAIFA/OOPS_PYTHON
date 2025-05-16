class Employee :

    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def display(self):
        print(f"Employee name: {self.name},Employee_id:{self.employee_id}")

class Department:
    def __init__(self,department,emp):
        self.department = department
        self.employee = emp

    def show(self):
        print(f"Department name :",self.department)
        self.employee.display()

emp1 = Employee("ali",23)
depart = Department("lahore",emp1)

emp1.display()
depart.show()
