# Defining a class
class Car:
    # Constructor method
    def __init__(self, make, model, year):
        self.make = make  # Attribute
        self.model = model  # Attribute
        self.year = year  # Attribute

    # Method (behavior)
    def start_engine(self):
        print(f"The {self.make} {self.model} is starting.")


# Creating an object (instance) of the class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing attributes
print(my_car.make)  # Output: Toyota

# Calling methods
my_car.start_engine()  # Output: The Toyota Corolla is starting.
