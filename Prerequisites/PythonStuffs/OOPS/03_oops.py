## 4. ENCAPSULATION : Available for me but not to the external world

# Modify the car class to encapsulate the brand attribute, making it private , and provide a getter

# Note : ( __ ) before an attribute make it private that accessable only inside the class



class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!" 
    
    def speed(self):
        print("100kmph")

class RacingCar(Car):
    def __init__(self, brand, model, mileage):     
         super().__init__(brand, model)
         self.mileage = mileage

    def speed(self):
        print("200kmph")

    # So a private attribute cannot be accessed anywhere except itw own clas and that too with __     
    # def brandVal(self):
    #     return f"The ${self.__brand} is very expensive"

    

myRacingCar = RacingCar("Lamborghini", "Model 1", 45)

# print(myRacingCar.__brand) # cant be accssed as the attribute is private
print(myRacingCar.get_brand())
print(myRacingCar.mileage)
# print(myRacingCar.brandVal())




## 5. POLYMORPHISM

# So it nothing but the different behavioor character of the same thing
# e.g. + can add number , concatenate strings


myNormalCar = Car("Toyota", "Fortuner")
myRaceCar = RacingCar("Bugati", "Cheron", 8)

print(myNormalCar.speed()) # 100kmph
print(myRaceCar.speed()) # 200kmph

# you see same method different result


