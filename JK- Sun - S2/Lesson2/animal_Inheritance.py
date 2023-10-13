#create a super class == class which will be stored some of common attributs and methods

class pets:
    def __init__(self, name, food, birthday):
        self.name = name
        self.food = food
        self.birthday = birthday

    def aboutpets(self):
        print(f"This is {self.name}, it was born in {self.birthday} and it likes {self.food}")


## SUb class == special class that will takes some of the attributes in the superclass
class cat(pets):
    def __init__(self, name, food, birthday, hobby): #Hobby is an attribut, only for cats class
        super().__init__(name,food,birthday)
        #we need to take the attributes in the super class
        self.hobby = hobby

    def aboutCat(self):
        print(f"This is my cat,{self.name}.It was born in {self.birthday} and it likes {self.food} and it's hobby is {self.hobby}")

cat1 = cat("Chicki","Dryfood","July 14th 2021","eating")
cat1.aboutCat()
cat1.aboutpets()