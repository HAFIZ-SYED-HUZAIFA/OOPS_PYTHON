# Engine class
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower} horsepower started.")

# Car class
class Car:
    def __init__(self, make, model, engine):
        self.make = make         
        self.model = model       
        self.engine = engine    

    def start_car(self):
        print(f"{self.make} {self.model} is starting.")
        self.engine.start()      


engine = Engine(150)  

car = Car("Toyota", "Corolla", engine)

car.start_car()
