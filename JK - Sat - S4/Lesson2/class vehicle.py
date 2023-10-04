class vehicle:
    def __init__(self, color, wheel, brand):
        self.color=color
        self.wheel = wheel
        self.brand = brand

    def about(self):
        print(f" this vehicle has {self.wheel} and it's manufactured by {self.brand} and has the gorgeous colour of {self.color}")

class car(vehicle):
    def __init__(self, color, wheel, brand, fuel_type,seater):
        super().__init__(self,color, wheel, brand)
        self.fuel = fuel_type
        self.seat = seater

    def aboutCar(self):
        print(f" this car has {self.seat} seats and manufactured by {self.brand} and has the gorgeous colour of {self.color} this car also runs on {self.fuel}" )

class bus(vehicle):
    def __init__(self, color, wheel, brand, capacity):
        super().__init__(color, wheel, brand)
        self.seats = capacity

    def aboutBus(self):
        print(f"This Bus was made by {self.brand} and has the capacity of {self.seats} People. This type comes in the colour {self.color}")

v1 = bus("red", 6, "Marcedes Benz", 120)
v1.aboutBus()