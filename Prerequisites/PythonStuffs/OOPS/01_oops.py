## 1. Basic Class and Object

# Create a car class with attributes like brand and model. Then create an instance of the class

class Bike : 
    brand = "RoyalEnfield",
    model = None

myBike = Bike()

# print(myBike)  

# Think class as a blank form
#Note : __init__ is a constructor means it is the first invoked when an object is made out of a class
class Car : 
    def __init__(self, userbrand, usermodel): #self hai telephone line or it's context or this in javascript
        self.brand = userbrand
        self.model =  usermodel

myCar = Car("Toyota" , "Corolla") #A filled form or using the form or created an instance or object

print(myCar.model)
myCar.model = "Hilux"
print(myCar.model)

print(myCar)