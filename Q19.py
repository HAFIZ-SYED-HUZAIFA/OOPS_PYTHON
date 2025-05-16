class Multiplier:
    def __init__(self,factor):
        self.factor = factor

    def __call__(self,number):
        return self.factor * number
        

obj1 = Multiplier(6)
print(obj1(2))
print(callable(obj1))
        
        