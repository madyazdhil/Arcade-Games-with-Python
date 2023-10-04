class Car:
    def __init__(self, make, model, year):
        self.make = make  # Property 1
        self.model = model  # Property 2
        self.year = year  # Property 3
        self.is_running = False  # Property 4 (default value)

    def start_engine(self):
        self.is_running = True  # Method 1
        return "Engine started."

    def stop_engine(self):
        self.is_running = False  # Method 2
        return "Engine stopped."

    def honk(self):
        return "Honk! Honk!"  # Method 3

    def get_age(self):
        current_year = 2023  # We assume the current year is 2023
        age = current_year - self.year
        return f"The car is {age} years old."

# Creating a Car object
my_car = Car("Toyota", "Camry", 2018)

# Accessing properties
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")

# Calling methods
print(my_car.start_engine())
print(my_car.honk())
print(my_car.get_age())
