class person:
    #nama, age, city , mata
    #blood, strenght, special
    #initialize the attributs (what that person has)
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    #creating a method = what that person can do
    def say_hello(self):
        return f"Hello, my name is {self.name}. nice to meet you"

    def birthday(self):
        return f"I'm {self.age} years old and my birthday is this month"

    def newcity(self):
        return f"Currently, I Lived in {self.city}"


ahmad123 = person("Ahmad",22, "New York")

print(ahmad123.say_hello())
print(ahmad123.birthday())
print(ahmad123.newcity())