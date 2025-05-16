class Employee :

    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

employee1 = Employee("Ali",200,11)
print(employee1.name)
print(employee1._salary)
print(employee1.__ssn)

