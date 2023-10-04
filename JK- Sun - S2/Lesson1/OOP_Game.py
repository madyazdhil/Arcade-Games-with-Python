class player:
    def __init__(self, name, Hp):
        self.name=name
        self.hp=Hp

    def attacked(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
            return f"{self.name} was attacked and lost {damage} liter of blood \nYou Dead Boy"
        else:
            return f"{self.name} was attacked and only had {self.hp} left"

p1 = player("Elytra", 210)
print(p1.attacked(30))
print(p1.attacked(190))