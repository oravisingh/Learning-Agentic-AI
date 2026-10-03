## 6. CLASS VARIABLE
# Add a class variable to Car that keeps track of the number of cars created

class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1 # or self.total_car
        # Since the constructor gets invoked evrytime an object is made with this class So we can pur logic of counting here

    def get_brand(self):
        return self.__brand + "!" 
    
    def speed(self):
        return "100kmph"

    ## 7. STATIC METHOD
    @staticmethod 
    def Static_thing(): # No self is linked here
        return "Cars are comfortable, beautiful and safe means of transport"

    @staticmethod
    def is_valid_model(model):
        return isinstance(model, str) and bool(model.strip())

    

print(Car.total_car)

Car("test", "test") # No need to reference an object to any variable in order to just invoke the class like an object is created but not stored/ referenced anywhere 
car2 = Car("testin", "test")

print(Car.total_car) # It is recommended to acess such variables directly by the class

print(car2.total_car) # Instance access reads the class variable; it does not create another Car.


## 7. STATIC METHODS : Methods that belong to the class itself but not any instace of it
# THe methods are accessible toevry instance of a class but methof=ds defined in an instance are only able to be accessed by that object of a class

# Add a static method to the Car class that returns a general description of a car

print(Car.Static_thing())
print(car2.Static_thing())

print(Car.is_valid_model("Sierra"))  # True
print(Car.is_valid_model("   "))    # False