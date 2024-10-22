class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


my_car = Car("Toyota", "Corolla")
my_car.start()
