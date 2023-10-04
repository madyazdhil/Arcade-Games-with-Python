class player:
    def __init__(self, name, initialBlood):
        self.name = name
        self.blood = initialBlood

    def attack(self, damage):
        if damage >= 0:
            self.blood -= damage
            if self.blood < 0:
                self.blood = 0
            return f"{self.name} was attacked and lost {damage} liter of blood"
        else:
            return "You input a negative number"

player1 = player("Epic Butterfly", 100)

print(player1.attack(50))
print(f"The blood remaining on {player1.name} is {player1.blood}")
print(player1.attack(20))
print(f"The blood remaining on {player1.name} is {player1.blood}")