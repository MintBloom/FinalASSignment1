
import random

class bcolors:  # {bcolors.HEADER} {bcolors.HEADER}
    # wrapping text in a print statement with these headers will change the colour of that terminal text in the terminal
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def enemy_picker(x):
    # depending on the value of x, an enemy is returned.
    list_of_enemies = {1:Slime, 2:Skeleton, 3:Goblin, 4:Golden_Unicorn}
    return list_of_enemies[x]

class Enemy:
    # class for BASIC enemies
    def __init__(self, name, min_dmg, max_dmg, hp=50):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.hp = hp

    def is_alive(self):
        # checks if enemy health is above 0
        return self.hp > 0

    def attack(self, player):
        # reduces the player's health by a specified amount
        damage = random.randint(self.min_dmg, self.max_dmg)
        print(f"{self.name} attacks {player.name} for {bcolors.HEADER}{damage} damage{bcolors.ENDC}!")
        player.take_damage(damage, player)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {bcolors.HEADER}{damage} damage{bcolors.ENDC}! (HP: {self.hp})")

class Slime(Enemy): # basic enemy
    def __init__(self, name="Slime", min_dmg=5, max_dmg=10, hp=20):
        super().__init__(name, min_dmg, max_dmg, hp)

class Goblin(Enemy): # basic enemy
    def __init__(self, name="Goblin", min_dmg=8, max_dmg=12, hp=20):
        super().__init__(name, min_dmg, max_dmg, hp)

class Skeleton(Enemy): # basic enemy
    def __init__(self, name="Skeleton", min_dmg=8, max_dmg=12, hp=20):
        super().__init__(name, min_dmg, max_dmg, hp)

class Golden_Unicorn(Enemy): # basic enemy
    def __init__(self, name="Golden Unicorn", min_dmg=10, max_dmg=15, hp=15):
        super().__init__(name, min_dmg, max_dmg, hp)
