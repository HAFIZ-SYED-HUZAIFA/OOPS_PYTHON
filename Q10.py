class Dog :
     def __init__(self,name,breed):
          self.name = name
          self.breed = breed

     def bark(self) :
          print(self.name,"is barking")   

dog1 = Dog("fluffy","none")
dog1.bark()  