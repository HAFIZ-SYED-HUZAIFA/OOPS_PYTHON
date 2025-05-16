def add_greetings(cls):
    def add_greet(self):
        print("helo from greet function")
    cls.greet = add_greet

    return cls
@add_greetings
class Person:
    def __init__(self,name):
        self.name = name

person1 = Person("ali")
person1.greet()
