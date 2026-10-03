## 2.CLASS METHOD AND SELF

#Add a method to the car class that displays the full name of the car.(brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    # 2.
    def fullName(self): #self hai telphone line 
        return f"{self.brand} {self.model}"

    # 4. 
    def get_brand(self):
        return self.brand + "!"

my_Car = Car("Tata", "Sierra")
print(my_Car.fullName())


## 3. INHERITENCE

# Create an Electric Car class that inherits from the Car class and has an additional attribute

class ElectricCar(Car): #Inheritence
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model) # Super mtlab upar parent se lelo
        self.batterySize = batterySize

myElectCar = ElectricCar("Tesla", "Model 5", "85kWh")
print(myElectCar.model)
print(myElectCar.fullName())


