# Define the parent class Player
class Player:
    def __init__(self, player_name, blood, attack_power):
        self.player_name = player_name
        self.blood = blood
        self.attack_power = attack_power

    def attack(self, enemy):
        print(f"{self.player_name} attacks {enemy.player_name} with {self.attack_power} attack power!")
        enemy.take_damage(self.attack_power)

    def take_damage(self, damage):
        self.blood -= damage
        print(f"{self.player_name} takes {damage} damage. Remaining blood: {self.blood}")

# Create child classes that inherit from Player
class Knight(Player):
    def __init__(self, player_name):
        super().__init__(player_name, 100, 20)  # Knights start with 100 blood and 20 attack power

    def shield_block(self):
        print(f"{self.player_name} raises their shield to block an attack!")

class Wizard(Player):
    def __init__(self, player_name):
        super().__init__(player_name, 80, 30)   # Wizards start with 80 blood and 30 attack power

    def cast_spell(self, enemy):
        spell_damage = 10
        print(f"{self.player_name} casts a powerful spell on {enemy.player_name}!")
        enemy.take_damage(spell_damage)

class Archer(Player):
    def __init__(self, player_name):
        super().__init__(player_name, 90, 25)   # Archers start with 90 blood and 25 attack power

    def shoot_arrow(self, enemy):
        arrow_damage = 15
        print(f"{self.player_name} shoots an arrow at {enemy.player_name}!")
        enemy.take_damage(arrow_damage)

class Assassin(Player):
    def __init__(self, player_name):
        super().__init__(player_name, 70, 35)   # Assassins start with 70 blood and 35 attack power

    def sneak_attack(self, enemy):
        sneak_damage = 40
        print(f"{self.player_name} performs a deadly sneak attack on {enemy.player_name}!")
        enemy.take_damage(sneak_damage)

# Create instances of child classes
knight = Knight("Sir Lancelot")
wizard = Wizard("Merlin")
archer = Archer("Robin Hood")
assassin = Assassin("Rina")

# Let the characters interact
knight.attack(wizard)
archer.attack(assassin)
wizard.cast_spell(knight)
assassin.sneak_attack(archer)

# Use unique methods of each class
knight.shield_block()
wizard.cast_spell(archer)
archer.shoot_arrow(knight)
assassin.sneak_attack(wizard)
