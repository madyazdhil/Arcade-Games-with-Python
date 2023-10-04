# Define the parent class Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"This is a {self.brand} {self.model}.")

# Create child classes that inherit from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"The {self.brand} {self.model} with {self.fuel_type} engine starts.")

class Bicycle(Vehicle):
    def __init__(self, brand, model, num_gears):
        super().__init__(brand, model)
        self.num_gears = num_gears

    def pedal(self):
        print(f"Pedaling the {self.brand} {self.model} with {self.num_gears} gears.")

class Boat(Vehicle):
    def __init__(self, brand, model, propulsion):
        super().__init__(brand, model)
        self.propulsion = propulsion

    def start_motor(self):
        print(f"Starting the {self.brand} {self.model} with {self.propulsion} propulsion.")

class Airplane(Vehicle):
    def __init__(self, brand, model, wingspan):
        super().__init__(brand, model)
        self.wingspan = wingspan

    def take_off(self):
        print(f"The {self.brand} {self.model} with a {self.wingspan}-foot wingspan takes off.")

# Create instances of child classes
car = Car("Toyota", "Camry", "gasoline")
bicycle = Bicycle("Giant", "Escape", 21)
boat = Boat("Mercury", "OceanPro", "outboard")
airplane = Airplane("Boeing", "747", 224)

# Describe the vehicles
car.describe()
bicycle.describe()
boat.describe()
airplane.describe()

# Use unique methods of each class
car.start_engine()
bicycle.pedal()
boat.start_motor()
airplane.take_off()
