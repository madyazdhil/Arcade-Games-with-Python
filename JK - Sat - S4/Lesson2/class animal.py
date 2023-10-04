# Define the parent class Animal
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print(f"I am {self.name}, a {self.species}.")


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

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Tabby")
# Let the animals introduce themselves
dog.introduce()
cat.introduce()


dog.bark()
cat.meow()
