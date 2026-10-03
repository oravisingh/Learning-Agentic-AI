## 8. Property Decorator
# Use a property decorator in the Car to make the model attributr read_only

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand + "!" 

    @property
    def model(self):
        return self.__model

myCar = Car("Honda","City")

# print(myCar.model)
# myCar.model = "Helena"
# print(myCar.model)
print(myCar.model) # the decorator has allowed us to access it as an attribute