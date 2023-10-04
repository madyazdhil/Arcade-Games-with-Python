# Define the parent class Fruit
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        print(f"This is a {self.color} {self.name}.")

# Create child classes that inherit from Fruit
class Apple(Fruit):
    def __init__(self, color, variety):
        super().__init__("apple", color)
        self.variety = variety

    def eat(self):
        print(f"Eating a {self.color} {self.variety} apple.")

class Banana(Fruit):
    def __init__(self, color, length):
        super().__init__("banana", color)
        self.length = length

    def peel(self):
        print(f"Peeling a {self.color} banana that is {self.length} inches long.")

class Orange(Fruit):
    def __init__(self, color, sweetness):
        super().__init__("orange", color)
        self.sweetness = sweetness

    def juice(self):
        print(f"Squeezing an {self.color} orange for its sweet juice.")

class Grape(Fruit):
    def __init__(self, color, seedless):
        super().__init__("grape", color)
        self.seedless = seedless

    def snack(self):
        if self.seedless:
            print(f"Popping some {self.color} seedless grapes as a snack.")
        else:
            print(f"Popping some {self.color} grapes as a snack.")

# Create instances of child classes
red_apple = Apple("red", "Fuji")
yellow_banana = Banana("yellow", 7)
orange_orange = Orange("orange", "very sweet")
purple_grape = Grape("purple", True)

# Describe the fruits
red_apple.describe()
yellow_banana.describe()
orange_orange.describe()
purple_grape.describe()

# Use unique methods of each class
red_apple.eat()
yellow_banana.peel()
orange_orange.juice()
purple_grape.snack()
