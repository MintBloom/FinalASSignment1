
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


class Sapphire_Golem(Boss_Enemy): # boss enemy
    def __init__(self, name="Sapphire Golem", min_dmg=25, max_dmg=30, no_of_turns=10, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Major Health Potion", 75, "A copious amount of a strange concoction, most likely brewed in a foreign land. It has a sweet aroma.", crafting = False),
            Weapon_Item("Sapphire Axe", 30, "Made from a shard of the Sapphire Golem itself. The construction is crude, but the blade is deathly sharp."),
            Health_Item("Disgusting Candy", -10, "A small, malleable piece of old candy covered in some goey substance. Perhaps it can be turned into something wonderful...")
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

    def attack(self, character, turn_number):
        if turn_number == self.no_of_turns:
            pass
        # i was trying to make a wipe machanic depending on the number of turns in the battle so far
        # reduces the player's health by a specified amount
        damage = random.randint(self.min_dmg, self.max_dmg)
        print(f"{self.name} attacks {character.name} for {bcolors.HEADER}{damage} damage{bcolors.ENDC}!")
        character.take_damage(damage)

class Bob_The_Assassin_King(Boss_Enemy): #boss enemy
    def __init__(self, name="Bob the Assassin King", min_dmg=15, max_dmg=20, no_of_turns=7, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Major Health Potion", 75, "A copious amount of a strange concoction, most likely brewed in a foreign land. It has a sweet aroma.", crafting = False),
            Weapon_Item("Swiftwood Daggers", 25, "Small but reliable dual-wielding weapon. It is well-made, legend says it was made by the Assassin King himself..."),
            Health_Item("Disgusting Candy", -10, "A small, malleable piece of old candy covered in some goey substance. Perhaps it can be turned into something wonderful...")
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

class Slime_Queen(Boss_Enemy): # boss enemy
    def __init__(self, name="Slime Queen", min_dmg=15, max_dmg=20, no_of_turns=10, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Major Health Potion", 75, "A copious amount of a strange concoction, most likely brewed in a foreign land. It has a sweet aroma.", crafting = False),
            Stat_Boost_Item("Jar of Slime", 5, 0, "desc"),
            Health_Item("Disgusting Candy", -10, "A small, malleable piece of old candy covered in some goey substance. Perhaps it can be turned into something wonderful...")
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

class Resurrected_Rubber_Ducky(Boss_Enemy):
    def __init__(self, name="Resurrected Rubber Ducky", min_dmg=10, max_dmg=10, no_of_turns=7, hp=50):
        super().__init__(name, min_dmg, max_dmg, no_of_turns, hp)
        self.enrage_toggle = False

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Major Health Potion", 75, "A copious amount of a strange concoction, most likely brewed in a foreign land. It has a sweet aroma.", crafting = False),
            Armour_Item("Ghost Armour Set", 15,"description"),
            Health_Item("Disgusting Candy", -10, "A small, malleable piece of old candy covered in some goey substance. Perhaps it can be turned into something wonderful...")
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

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