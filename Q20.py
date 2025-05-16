class InvalidAgeError(Exception):
    pass

class AgeChecker :
    def __init__(self,age):
        self.age = age

    def check_age(self):
        try :
            if self.age < 18 :
                raise InvalidAgeError("age invalid")
            print("adult")
        except InvalidAgeError as e:
            print(f"Error message :", e)




age1 = AgeChecker(53)
age1.check_age()

