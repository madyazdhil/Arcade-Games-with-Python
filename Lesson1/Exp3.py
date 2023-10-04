class Person:
    def __init__(self, name, age, city):
        self.name = name  # Property 1
        self.age = age  # Property 2
        self.city = city  # Property 3

    def say_hello(self):
        return f"Hello, my name is {self.name}."  # Method 1

    def celebrate_birthday(self):
        self.age += 1  # Method 2
        return f"Happy {self.age}th birthday!"

    def relocate(self, new_city):
        self.city = new_city  # Method 3
        return f"{self.name} has moved to {new_city}."

# Creating a Person object
person = Person("Alice", 30, "New York")

# Accessing properties
print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"City: {person.city}")

# Calling methods
print(person.say_hello())
print(person.celebrate_birthday())
print(person.relocate("Los Angeles"))
