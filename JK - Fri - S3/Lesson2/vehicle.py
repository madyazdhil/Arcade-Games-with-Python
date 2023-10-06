class vehicle:
    def __init__(self, brand, seater,fuel):
        self.brand = brand
        self.seater = seater
        self.fuel = fuel
    def about(self):
        print(f"This is a car made by {self.brand} and it has {self.seater} and run by {self.fuel}")

class car(vehicle):
    def __init__(self, brand, seater,fuel,type ):
        super().__init__(brand, seater,fuel)
        self.type = type

    def carSpecs(self):
        print(f"This is {self.type} is a car by {self.brand} with{self.seater} run by {self.fuel}")

c1 = car("audi", 7, "Hybrid", "SUV")
c1.carSpecs()