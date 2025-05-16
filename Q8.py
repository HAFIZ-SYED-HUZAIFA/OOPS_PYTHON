class Person :
    def __init__(self,name):
        self.name = name
        
class Teacher(Person) :
    def __init__(self, name , subject):
        super().__init__(name)
        self.subject = subject

    def display(self) :
        print(self.name)
        print(self.subject)

t1 = Teacher("ali","eng")

print(t1.name)
t1.display()

