
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

def boss_picker(x):
    # depending on the value of x, an enemy is returned.
    list_of_bosses = {1:Sapphire_Golem, 2:Slime_Queen, 3:Bob_The_Assassin_King, 4:Resurrected_Rubber_Ducky}
    return list_of_bosses[x]

class Boss_Enemy:
    # class for BOSS enemies
    def __init__(self, name, min_dmg, max_dmg, no_of_turns, hp=50):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.hp = hp
        self.no_of_turns = no_of_turns

    def is_alive(self):
        # checks if enemy health is above 0
        return self.hp > 0
    
    def check_turn(self, turn_number):
        if turn_number == self.no_of_turns:
            print("")
            input("")
            return True
        else:
            return False

    def attackplayer(self, character):
        # i was trying to make a wipe machanic depending on the number of turns in the battle so far
        # reduces the player's health by a specified amount
        damage = random.randint(self.min_dmg, self.max_dmg)
        print(f"{self.name} attacks {character.name} for {bcolors.HEADER}{damage} damage{bcolors.ENDC}!")
        character.take_damage(damage, character)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {bcolors.HEADER}{damage} damage{bcolors.ENDC}! (HP: {self.hp})")


class Sapphire_Golem(Boss_Enemy): # focuses on simple big damage
    def __init__(self, name="Sapphire Golem", min_dmg=25, max_dmg=30, no_of_turns=10, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)

    def attack(self, character, turn_number):
        if turn_number == self.no_of_turns:
            pass
        # i was trying to make a wipe machanic depending on the number of turns in the battle so far
        # reduces the player's health by a specified amount
        damage = random.randint(self.min_dmg, self.max_dmg)
        print(f"{self.name} attacks {character.name} for {bcolors.HEADER}{damage} damage{bcolors.ENDC}!")
        character.take_damage(damage)

class Bob_The_Assassin_King(Boss_Enemy): # focuses on critical damage
    def __init__(self, name="Bob the Assassin King", min_dmg=15, max_dmg=20, no_of_turns=7, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)

class Slime_Queen(Boss_Enemy): # focuses on tick damage
    def __init__(self, name="Slime Queen", min_dmg=15, max_dmg=20, no_of_turns=10, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)

class Resurrected_Rubber_Ducky(Boss_Enemy): # focuses on an enrage mechanic 
    def __init__(self, name="Resurrected Rubber Ducky", min_dmg=10, max_dmg=10, no_of_turns=7, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)
        self.enrage_toggle = False

    def attack(self, character):
        if self.hp <= 35 and self.enrage_toggle == False:
            self.enrage_toggle = True
            self.hp += 30
            self.min_dmg += 20
            self.max_dmg += 20
            print(f"{self.name} is ENRAGED. \n +30 health, now up to {self.hp} hp. \n +20 damage, now {self.max_dmg} damage. ")
            return
        damage = random.randint(self.min_dmg, self.max_dmg)
        print(f"{self.name} attacks {character.name} for {bcolors.HEADER}{damage} damage{bcolors.ENDC}!")
        character.take_damage(damage)