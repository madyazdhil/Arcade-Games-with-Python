class car:
    def __init__(self, color, model, seat):
        self.color = color
        self.model = model
        self.seat = seat

    def Move(self):
        return f"The car with colour {self.color} can move for 100km in one charge"

    def type(self):
        return f"The car with {self.model} has {self.seat} Seater available"

car1 = car("Red", "Sedan", 5)

print(car1.Move())