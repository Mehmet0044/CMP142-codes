class Phone:

    
    def __init__(self, color, brand, password):
        self.color = color                   
        self._brand = brand                  
        self.__password = password             

    def call(self): 
        
        return "The " + self.color + " " + self._brand + " is ringing"


person1 = Phone("Black", "Apple Phone", "Highly confidential")
person2 = Phone("White", "Samsung Phone", "Top Secret")
p1 = Phone("red", "Redmi Phone", "xxxxx")

print(person1.color)               
print(person2._brand)              
print(p1._Phone__password)         

print(person1.call())              
