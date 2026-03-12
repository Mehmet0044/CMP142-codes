from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    def __init__(self, tires):
        self.tires = tires
        
    @abstractmethod
    def start(self):
        pass
            
    def display(self):
        print("vehicle with", self.tires, "tires")
            
class Bike(Vehicle):
    
    def __init__(self, color):
        super().__init__(2)
        self.color = color
        
    def start(self):
        print("start with kick")
        

class Scooty(Vehicle):
    
    def __init__(self):
        super().__init__(2)
        
    def start(self):
        print("self start")
        
class Car(Vehicle):
    
    def __init__(self):
        super().__init__(4)
        
    def start(self):
        print("start with key")
       
class Truck(Vehicle):

    def __init__(self):
        super().__init__(6)

    def start(self):
        print("truck starts with button")
        

my_bike = Bike("Black")
my_bike.start()
my_bike.display()

my_scooty = Scooty()
my_scooty.start()

my_car = Car()
my_car.start()

my_truck = Truck()
my_truck.start()
my_truck.display()