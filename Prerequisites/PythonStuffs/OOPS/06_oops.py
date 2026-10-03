## 9. CLASS INHERITENCE AND ISISNSTANCE() FUNCTION
#Demonstrate the use of isinstance() to check if myElectCar is an instance of Car and ElectricCar

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    # 2.
    def fullName(self): #self hai telphone line 
        return f"{self.__brand} {self.model}"

    # 4. 
    def get_brand(self):
        return self.__brand + "!"


## 3. INHERITENCE

# Create an Electric Car class that inherits from the Car class and has an additional attribute

class ElectricCar(Car): #Inheritence
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model) # Super mtlab upar parent se lelo
        self.batterySize = batterySize

myElectCar = ElectricCar("Tesla", "Model 5", "85kWh")
print(myElectCar.model)
print(myElectCar.fullName())


print(isinstance(myElectCar, Car)) # (object, class)
print(isinstance(myElectCar, ElectricCar))

## 10. MULTIPLE INHERITENCE
# Create two classes Battery and Engine and let the ElectricCar class inherit from both demonstrating multiple inheritence

print("MULTIPLE INHERITENCE")

class Battery:
    def __init__(self, battery):
        self.battery = battery

class Engine:
    def __init__(self, engine):
        self.engine = engine

class ElectricCar2(Battery, Engine, Car):
    def __init__(self, battery, engine, brand, model):
        Battery.__init__(self, battery)
        Engine.__init__(self, engine)
        Car.__init__(self, brand, model)
        

myNewTesla = ElectricCar2("80kwh", "500hp", "Tesla", "model-V")
                          
print(myNewTesla.battery)
print(myNewTesla.engine)
print(myNewTesla.model)
print(myNewTesla.get_brand())