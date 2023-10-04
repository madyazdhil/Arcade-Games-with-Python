class person:
    def __init__(self, name, age, religion, gender, personality):
        self.name = name
        self.age = age
        self.religion = religion
        self.gender = gender
        self.personality = personality

    def intoduce(self):
        return f"Hello my name is {self.name} I'm a {self.religion} and I'm a {self.personality}"

    def healthStats(self):
        return f"I'm {self.age} and a Healthy {self.gender}"


person1 = person("andrian", 21, "Islam", "Male", "Introvert")
print(person1.intoduce())