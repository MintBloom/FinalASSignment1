
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

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Minor Healing Potion", 20, "A strange concoction, most likely brewed in a foreign land. It has a sweet aroma."),
            Stat_Boost_Item("Jar Of Slime", 5, 0, "desc"),
            Stat_Boost_Item("Slime Droplet", 0, 0, "Does not grant any buff in its current state. Perhaps it can be used to craft with."),
            Health_Item("Disgusting Candy", -10, "A small, malleable piece of old candy covered in some goey substance. Perhaps it can be turned into something wonderful...")
        ]
        list_of_loot = random.sample(item_list, k=2)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

class Goblin(Enemy): # basic enemy
    def __init__(self, name="Goblin", min_dmg=8, max_dmg=12, hp=20):
        super().__init__(name, min_dmg, max_dmg, hp)

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Minor Healing Potion", 20, "A strange concoction, most likely brewed in a foreign land. It has a sweet aroma."),
            Weapon_Item("Goblin Sword", 20, "A sword forged in the Heart of Goblin Nests. It is in not in great shape, but will do plenty damage."),
            Stat_Boost_Item("Goblin Eye", 3, 3, "desc"),
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

class Skeleton(Enemy): # basic enemy
    def __init__(self, name="Skeleton", min_dmg=8, max_dmg=12, hp=20):
        super().__init__(name, min_dmg, max_dmg, hp)

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Minor Healing Potion", 20, "A strange concoction, most likely brewed in a foreign land. It has a sweet aroma."),
            Shield_Item("Bone Shield", 10, "description"),
            Stat_Boost_Item("Skeleton Bone Marrow", 0, 4, "desc"),
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")

class Golden_Unicorn(Enemy): # basic enemy
    def __init__(self, name="Golden Unicorn", min_dmg=10, max_dmg=15, hp=15):
        super().__init__(name, min_dmg, max_dmg, hp)

    def drop(self, player):
        # picks the drops that the player will recieve for killing this enemy
        item_list = [
            Health_Item("Minor Healing Potion", 20, "A strange concoction, most likely brewed in a foreign land. It has a sweet aroma."),
            Shield_Item("Bone Shield", 10, "description"),
            Weapon_Item("Gold Spear", 25, "With the unicorn's horn as a tip, this spear does not miss it's mark."),
        ]
        list_of_loot = random.sample(item_list, k=1)
        for i in list_of_loot:
            player.inventory.append(i)
            print(f"{self.name} dropped {bcolors.OKGREEN}{i.name}{bcolors.ENDC}! It was added to your inventory.")