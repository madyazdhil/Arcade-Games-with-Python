# SUPER CLASS -- A CLASS WHERE WE TOOK the original attributes and methods
class animal:
    def __init__(self, name, age, legs, color):
        self.name = name
        self.age = age
        self.legs = legs
        self.color = color

    def about(self):
        print(f"This is {self.name}, my pet with {self.legs} legs and it has a gorgeous {self.color}")

# SUB-CLASS == THE CHILD OF THE SUPER CLASS

class dog(animal):
    def __init__(self, name, color, breed):
        super().__init__(name, age=None, legs=None, color=color)  # Removed age and legs parameters
        self.breed = breed

    def about(self):
        super().about()  # Call the parent class about method
        print(f"This is {self.name}, a very cute {self.breed}")

animal1 = dog("Fira", "Grey", "Corgi")

animal1.about()
