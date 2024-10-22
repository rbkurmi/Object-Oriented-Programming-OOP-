from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # This method is abstract

# Concrete class
class Car(Vehicle):
    def start_engine(self):
        print("The car's engine is starting.")

car = Car()
car.start_engine()  # Output: The car's engine is starting.
