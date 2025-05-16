class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self) :
        print(f"student name is :", self.name)
        print(f"student marks is :" , self.marks)

s1 = Student("ali",90)
s1.display()

