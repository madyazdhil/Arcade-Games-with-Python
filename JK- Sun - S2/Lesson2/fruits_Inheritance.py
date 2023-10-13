#superclass
class fruit:
    def __init__(self, color, harvest):
        self.col = color
        self.harv = harvest

    def about(self):
        print(f" This fruit's color is {self.col} and has been harvested in {self.harv}.")


#subclass
class orange(fruit):
    def __init__(self, color, harvest, originated):
        super().__init__(color,harvest)
        self.ori = originated

    def aboutOrange(self):
        print(f"This Orange was originated from {self.ori} has a unique {self.col} color and harvested during {self.harv} season")

class melon(fruit):
    def __init__(self, color, harvest, size):
        super().__init__(color,harvest)
        self.size = size

    def aboutMelon(self):
        print(f"This has a unique {self.col} color and harvested during {self.harv} season. It has a {self.size} size characteristics")



