class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This car is a {self.make} {self.model}")


# Creating an object of the class
my_car = Car("Toyota", "Corolla")
my_car.display_info()