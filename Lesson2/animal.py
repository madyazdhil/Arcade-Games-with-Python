# Define the parent class Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"I am {self.name}, a {self.species}.")

# Create child classes that inherit from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "dog")
        self.breed = breed

    def bark(self):
        print(f"{self.name} (a {self.breed} dog) barks loudly!")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "cat")
        self.color = color

    def meow(self):
        print(f"{self.name} (a {self.color} cat) meows softly.")

class Fish(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def swim(self):
        print(f"{self.name} (a {self.color} fish) swims gracefully in the water.")

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} (a {self.species} with a {self.wingspan}-inch wingspan) soars through the sky.")

# Create instances of child classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")
fish = Fish("Nemo", "Clownfish", "orange")
bird = Bird("Hawk", "Hawk", 50)

# Let the animals introduce themselves
dog.introduce()
cat.introduce()
fish.introduce()
bird.introduce()

# Use unique methods of each class
dog.bark()
cat.meow()
fish.swim()
bird.fly()
