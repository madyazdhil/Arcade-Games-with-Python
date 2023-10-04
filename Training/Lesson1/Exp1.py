class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Property 1
        self.breed = breed  # Property 2
        self.age = age  # Property 3

    def bark(self):
        return "Woof, woof!"  # Method 1

    def eat(self, food):
        return f"{self.name} is eating {food}"  # Method 2

    def age_in_human_years(self):
        human_age = self.age * 7  # Method 3
        return f"{self.name} is {human_age} years old in human years"


# Creating a Dog object [1]
my_dog = Dog("Buddy", "Golden Retriever", 3)

# Creating a Dog object [2]
#my_dog2 = Dog()
#my_dog2.name = "Billy"
#my_dog2.breed = "Pitbull"
#my_dog2.age = 2

# Accessing properties
print(f"Name: {my_dog.name}")
print(f"Breed: {my_dog.breed}")
print(f"Age: {my_dog.age}")

# Calling methods
print(my_dog.bark())
print(my_dog.eat("kibble"))
print(my_dog.age_in_human_years())
