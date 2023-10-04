class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class child1(Person):
    def __init__(self,name,age, talent):
        super().__init__(name,age)
        self.talent=talent

    def ability(self):
        return f" My son, {self.name} has a talent which is {self.talent}"

c1 = child1("adrian",12,"Singing")
print(c1.ability())