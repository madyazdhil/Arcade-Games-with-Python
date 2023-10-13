#super class
class animal:
    def __init__(self, name, kingdom, live):
        self.name = name
        self.kingdom = kingdom
        self.live = live

    def about(self):
        print(f"This animal's name is {self.name} and it cames from {self.kingdom} anad live in {self.live}")

#sub-class

class dog(animal):
    def __init__(self,name, kingdom, live, breed):
        super().__init__(name,kingdom,live)
        self.breed = breed

    def aboutdog(self):
        print(f"This dog is a {self.breed}, and it's name is {self.name}")

class bird(animal):
    def 

d1 = dog(name="CHici", kingdom=None, live=None, breed = "Pitbull")
d1.aboutdog()


