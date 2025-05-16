class Product:
    def __init__(self,price):
        self._price = price

    @property
    def name(self):
        return self._price
    
    @name.setter
    def name(self,new_price):
        if new_price >= 0 :

            self._price = new_price
        else:
            print("value negative nhi honi chayee")

    @name.deleter
    def name(self):
        del self._price

obj1 = Product(9)
print(obj1._price)
obj1._price = 7
print(obj1._price)
del obj1._price
# print(obj1._price)