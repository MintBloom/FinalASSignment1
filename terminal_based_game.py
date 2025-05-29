

# implement consumables
# expand inventory and introduce crafting
# save/load functionality

# to dos for code presentation:
# implement unit tests
# high quality coding standards
# documentation via. README and comments



import random, sys, os, pickle

###########################################################################################################################################################
# Making the game look pretty
###########################################################################################################################################################

def clear_terminal():
    # clears the terminal of any previous text
    if sys.platform == "win32":
        # for windows os
        os.platform("cls")
    else:
        # for other os; namely linux and this should work for macos
        os.system("clear")


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

##########################################################################################################################################################
# Item Classes
##########################################################################################################################################################
class Item:
    def __init__(self, name, description, crafting):
        self.name = name
        self.description = description
        self.crafting = crafting # determines whether an item can be used for crafting (True) or not (False)

    def string(self):
        # returns an item's name and it's description
        return f"{self.name}: {self.description}" if self.description else self.name
    
    def crafting_status_toggle(self):
        # changes the crafting status of an object
        if self.crafting == True:
            self.crafting == False
        else:
            self.crafting == True
    
class Weapon_Item(Item):
    def __init__(self, name, damage=0, description="", crafting = False):
        super().__init__(name, description, crafting)
        self.damage = damage

class Shield_Item(Item):
    def __init__(self, name, defence=0, description="", crafting = False):
        super().__init__(name, description, crafting)
        self.defence = defence

class Armour_Item(Item):
    def __init__(self, name, defence=0, description="", crafting = False):
        super().__init__(name, description, crafting)
        self.defence = defence
    
class Stat_Boost_Item(Item):
    def __init__(self, name, attack_dmg=0, defence_amount=0, description="", crafting = True):
        super().__init__(name, description, crafting)
        self.attack_dmg = attack_dmg  # attack damage the item adds
        self.defence_amount = defence_amount  # defence amount the item adds
    
    def add_bonus(self, player):
        # any extra defence power will be added to the player's defence_bonus stat. This can only be done if the player has a shield
        for i in player.equipped_items:
            if isinstance(i, Shield_Item): 
                # if the item in the list is an object belonging to the Shield_Item class, True is added to the true_false list
                player.defence_bonus += self.defence_amount
                player.attack_bonus += self.attack_dmg
                print(f"{player.name} has gained {self.defence_amount} defence bonus.\n{player.name} has gained {self.attack_dmg} attack bonus.")
                return True
            else:
                continue
        return False

class Health_Item(Item):
    def __init__(self, name, health_amount=0, description="", crafting = True):
        super().__init__(name, description, crafting)
        self.health_amount = health_amount

    def apply_health(self, player):
        # increases player hp by the specific item amount
        player.hp += self.health_amount

####################################################################################################################################################
# Character Class
#####################################################################################################################################################
class Character:
    def __init__(self, name, hp=100, attack_bonus=0, defence_bonus=0):
        self.name = name
        self.hp = hp
        self.attack_bonus = attack_bonus
        self.defence_bonus = defence_bonus
        self.inventory = []  # Inventory holds Item objects in this list
        self.equipped_items = [] # Equipped_items hold 

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy, item_damage=0):
        damage = self.attack_bonus + item_damage
        print(f"{self.name} attacks {enemy.name} for {bcolors.HEADER}{damage} damage{bcolors.ENDC}!")
        enemy.take_damage(damage)

    def take_damage(self, damage, player):
        self.hp -= damage
        self.hp += player.defence_bonus
        print(f"{self.name} takes {bcolors.HEADER}{damage} damage{bcolors.ENDC}! (HP: {self.hp})")

    def add_item(self, item):
        # adds item to inventory list
        self.inventory.append(item)
        
    def remove_item(self, item):
        # removes item from inventory list
        self.inventory.remove(item)

    def show_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("  (empty)")
        else:
            for item in self.inventory:
                print(f"  --> {item.string()}")

    def equip_item(self, item):
        # adds item to equipped_items list
        self.equipped_items.append(item)

    def unequip_item(self, item):
        # removes item from equipped_items list
        self.equipped_items.remove(item)

    def show_equipped_items(self):
        print("Equipped Items:")
        if not self.equipped_items:
            print("  (empty)")
        else:
            for item in self.equipped_items:
                print(f"  --> {item}")
    
###################################################################################################################
# Enemy Classes
###################################################################################################################
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
######################################################################################################################################
# Game Functions
######################################################################################################################################

def cycle_through_items(desired_item, player):
    for item in player.inventory:
        if item.name == desired_item:
            return True
        else:
            continue
    return False

def crafting_menu(player):
    # menu for crafting, and where items are removed and added from inventory
    while True:
        clear_terminal()
        print(f"\nCrafting Items in your inventory:\nPress x to exit")
        crafting_list = [] # temporary list to store player's inventory items that can be used for crafting
        for item in player.inventory:
            if item.crafting == True:
                crafting_list.append(item.name) # adds item to the crafting_list
                print(item.string()) # prints item for user
            else:
                continue
        if not crafting_list:
            print("You have no items in your inventory that can be used for crafting.")
            input("")
            return
        print("\nCrafting Menu:") # MAKE MENU LOOK PRETTY
        print("Minor Healing Potion x3 ---> Major Healing Potion")
        print("Disgusting Candy + Jar of Slime ---> Minor Healing Potion")
        print("Jar of Slime + Goblin Eye ---> Elixir of Exuberance")
        print("Skeleton Bone Marrow + Goblin Eye ---> Elixir of Sorrow")
        print("Slime Droplet + Slime Droplet ---> Jar of Slime\n")
        choice = input("").title().strip()
        if choice == "Major Healing Potion":
            if crafting_list.count("Minor Healing Potion") == 3:
                for item in player.inventory:
                    # first loop to check for item
                    if item.name == "Minor Healing Potion":
                        player.remove_item(item)
                        break
                    else:
                        continue
                for item in player.inventory:
                    # second loop to check for second item
                    if item.name == "Minor Healing Potion":
                        player.remove_item(item)
                        break
                    else:
                        continue
                for item in player.inventory:
                    # second loop to check for second item
                    if item.name == "Minor Healing Potion":
                        player.remove_item(item)
                        break
                    else:
                        continue
                player.add_item(Health_Item("Major Health Potion", 75, "A copious amount of a strange concoction, most likely brewed in a foreign land. It has a sweet aroma.", crafting = False)) # new item added
                print(f"{choice} has been crafted! It has been added to your inventory.")
                input("")
            else:
                print("You do not have all of the right items to craft Major Healing Potion.")
                input("")     
        elif choice == "Minor Healing Potion":
            if cycle_through_items("Disgusting Candy", player) and cycle_through_items("Jar Of Slime", player):
                for item in player.inventory:
                    # first loop to check for item
                    if item.name == "Disgusting Candy":
                        player.remove_item(item)
                        print("item removed")
                        break
                    else:
                        continue
                for item in player.inventory:
                    # second loop to check for second item
                    if item.name == "Jar Of Slime":
                        player.remove_item(item)
                        print("item removed")
                        break
                    else:
                        continue
                player.add_item(Health_Item("Minor Healing Potion", 15, "A strange concoction, most likely brewed in a foreign land. It has a sweet aroma.")) # new item added
                print(f"{choice} has been crafted! It has been added to your inventory.")
                input("")
            else:
                print("You do not have all of the right items to craft Minor Healing Potion.")
                input("")
        elif choice == "Elixir Of Sorrow":
            if cycle_through_items("Skeleton Bone Marrow", player) and cycle_through_items("Goblin Eye", player):
                for item in player.inventory:
                    # first loop to check for item
                    if item.name == "Skeleton Bone Marrow":
                        player.remove_item(item)
                        break
                    else:
                        continue
                for item in player.inventory:
                    # second loop to check for second item
                    if item.name == "Goblin Eye":
                        player.remove_item(item)
                        break
                    else:
                        continue
                player.add_item(Stat_Boost_Item("Elixir Of Sorrow", 10, 10, "Using the sorrow of a bygone era, this elixir boosts attack and defence equally", False)) # new item added
                print(f"{choice} has been crafted! It has been added to your inventory.")
                input("")
            else:
                print("You do not have all of the right items to craft Elixir of Sorrow.")
                input("")
        elif choice == "Jar Of Slime":
            if crafting_list.count("Slime Droplet") == 2:
                for item in player.inventory:
                    # first loop to check for item
                    if item.name == "Slime Droplet":
                        player.remove_item(item)
                        break
                    else:
                        continue
                for item in player.inventory:
                    # second loop to check for second item
                    if item.name == "Slime Droplet":
                        player.remove_item(item)
                        break
                    else:
                        continue
                player.add_item(Stat_Boost_Item("Jar Of Slime", 5, 0, "desc", False)) # new item added
                print(f"{choice} has been crafted! It has been added to your inventory.")
                input("")
            else:
                print("You do not have all of the right items to craft Jar of Slime.")
                input("")
        elif choice == "Elixir Of Exuberance":
            if cycle_through_items("Jar Of Slime", player) and cycle_through_items("Goblin Eye", player):
                for item in player.inventory:
                    # first loop to check for item
                    if item.name == "Jar Of Slime":
                        player.remove_item(item)
                        break
                    else:
                        continue
                for item in player.inventory:
                    # second loop to check for second item
                    if item.name == "Goblin Eye":
                        player.remove_item(item)
                        break
                    else:
                        continue
                player.add_item(Stat_Boost_Item("Elixir Of Exuberance", 15, 5, "desc", False)) # new item added
                print(f"{choice} has been crafted! It has been added to your inventory.")
                input("")
            else:
                print("You do not have all of the right items to craft Elixir of Exuberance.")
                input("")
        elif choice in ("x", "X"):
            return        
        else:
            print(f"'{choice}' not found. Make sure everything is spelled correctly.")
            input("")

#######################################################################################################################################

def consuming_item(player):
    # allows the player to consume an item - removes specified item from inventory and applies effect 
    clear_terminal()
    while True:
        print("\nWhat would you like to consume?\nPress x exit")
        consumable_list = [] # create temporary list to hold all consumables items that the player has
        for item in player.inventory:
            # checks whether the current item in inventory is a health or stat boosting item
            if isinstance(item, Health_Item) or isinstance(item, Stat_Boost_Item):
                
                consumable_list.append(item)
                print(item.string())
            else:
                continue
        if not consumable_list:
            print("You have no consumables")
            input("")
            return 
        choice = input(" --> ").title().strip()
        if choice in ("x", "X"): return
        for item in consumable_list:
            if isinstance(item, Health_Item) and choice == item.name:
                item.apply_health(player)
                player.remove_item(item)
                return
            elif isinstance(item, Stat_Boost_Item) and choice == item.name:
                item.add_bonus # add defence
                player.remove_item(item) if item.add_bonus(player) == True else print("You have no shield equipped; defence cannot be increased.")
                input("")
                return
            elif choice == "x":
                return
            else:
                continue
        print(f"'{choice}' not found. Make sure everything is spelled correctly.")
        input("")

def equip_item(player):
    # menu to equip an armour, weapon or shield
    clear_terminal()
    while True:
        print("\nWhat would you like to equip?\nPress x to exit\n")
        equippable_item_list = [] # create temporary list to hold all equippable items from the player's current inventory
        for item in player.inventory:
            # checks whether the player has any equippable items in their inventory
            if isinstance(item, Shield_Item) or isinstance(item, Armour_Item) or isinstance(item, Weapon_Item):
                equippable_item_list.append(item) # adds equippable item
                print(f"--{item.string()}") # print name and desc of that item
            else:
                continue # skip to the next iteration of the for loop
        if not equippable_item_list:
            # if no equippable item is found, the player is sent back to the inventory menu
            print("You have no equippable items")
            input("")
            return
        # if an equippable item is found the player can search for an item of their choice
        choice = input(" --> ").title().strip()
        if choice in ("x", "X"): return
        for item in equippable_item_list:
            # this for loop searches the list of equippable items for a match of what the player has searched for
            if isinstance(item, Shield_Item) and choice == item.name or isinstance(item, Armour_Item) and choice == item.name or isinstance(item, Weapon_Item) and choice == item.name:
                # if a match is found, a search is conducted for an already equipped item of the same type
                for equipped_item in player.equipped_items:
                    # this for loop checks whether the player already has an item of the same type already equipped
                    if type(item) == type(equipped_item):#### fix how to find whether an item type is already equipped or not
                        print(f"You already have another item of the same class equipped {equipped_item.name}. Cannot have multiple items of the same type equipped at the same time.")
                        input("")
                        return
                    else:
                        continue
                player.equip_item(item) #_item(item)
                player.remove_item(item) # removes item from inventory
                print(f"{item.name} is now equipped!")
                return
            else:
                continue
        print(f"'{choice}' not found. Make sure everything is spelled correctly.")
        input("")

def unequip_item(player):
    # this function includes the whole process of allowing the player to unequip an item
    clear_terminal()
    while True:
        print("What would you like to unequip?\nPress x to exit")
        print(player.equipped_items)
        for item in player.equipped_items:
            # checks whether the player has any equippable items in their inventory
            print(f"--{item.string()}")################################here
        choice = input(" --> ").title().strip()
        if choice in ("x", "X"): return        
        for item in player.equipped_items:
            if isinstance(item, Shield_Item) and choice == item.name or isinstance(item, Armour_Item) and choice == item.name or isinstance(item, Weapon_Item) and choice == item.name:
                player.unequip_item(item)
                player.add_item(item)
                print(f"{item.name} has been unequipped.")
                input("")
                return
            else:
                continue # skip to the next iteration of the for loop
        print(f"'{choice}' not found. Make sure everything is spelled correctly.")
        input("")

def inventory_menu(player):
    clear_terminal()
    while True:
        print("\n")
        player.show_inventory()
        print("1. Consume an Item")
        print("2. Equip an Item")
        print("3. Unequip Item")
        print("4. Exit Inventory")
        answer = input("")
        if answer == "1":
            # consuming item menu
            consuming_item(player)
            return
        elif answer =="2":
            # equip an item menu
            equip_item(player)
        elif answer == "3":
            # unequip item menu
            unequip_item(player)
        elif answer == "4":
            return   # Skip enemy turn to allow further action after checking inventory.
        else:
            print("Invalid Input.")

def enemy_picker(x):
    # depending on the value of x, an enemy is returned.
    list_of_enemies = {1:Slime, 2:Skeleton, 3:Goblin, 4:Golden_Unicorn}
    return list_of_enemies[x]

def boss_picker(x):
    # depending on the value of x, an enemy is returned.
    list_of_bosses = {1:Sapphire_Golem, 2:Slime_Queen, 3:Bob_The_Assassin_King, 4:Resurrected_Rubber_Ducky}
    return list_of_bosses[x]

def combat(player, enemy):
    # covers the combat loop for the BASIC enemy types
    clear_terminal()
    print(f"\nA wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        print(f"\nThe {enemy.name} stands before you.")
        # Player's turn
        print("\nYour turn:")
        print("1. Attack")
        print("2. Show Inventory")
        print("3. Parry and Counter")
        print("4. Current Stats")
        match input("Choose your action: "):
            # action depending on player choice
            case '1':
                # player chooses to attack
                true_false = []
                for i in player.equipped_items:
                    if isinstance(i, Weapon_Item): 
                        # if the item in the list is an object belonging to the Weapon_Item class, True is added to the true_false list
                        true_false.append(True)
                        item_damage = i.damage
                    else:
                        # if the item is anything else, False is added to the true_false list
                        true_false.append(False)
                if any(true_false):
                    print("Weapon Equipped.")
                    player.attack(enemy, item_damage)                    
                else:
                    print("You have no weapon equipped.")
                    input("")
                    continue
            case '2':
                # interact with inventory
                inventory_menu(player)
                continue
            case '3':
                # player chooses to defend counter attack
                true_false = []
                for i in player.equipped_items:
                    if isinstance(i, Shield_Item): 
                        # if the item in the list is an object belonging to the shield_Item class, 1 is added to the true_false list
                        true_false.append(1)
                    if isinstance(i, Weapon_Item):
                        true_false.append(2)
                    else:
                        true_false.append(0)
                if any(x == 1 for x in true_false) and any(x == 2 for x in true_false):
                    # in other words, if a shield is equipped and a sword is equipped, the player has a chance to defend and counter attack 
                    print("Shield Equipped.\nWeapon Equipped.")
                    if random.random() < 0.5: # random.random() generates a random float between 0.0 and 1.0
                        print(f"{player.name} successfully parried!")
                        if random.random() < 0.5:
                            print(f"{player.name} successfully counter attacked!")
                            player.attack(enemy, item_damage)
                            input("")
                            continue
                        print(f"{enemy.name} blocked {player.name}'s counter attack!")
                        continue
                    else:
                        print(f"{player.name} was unable to defend!")
                        enemy.attack(player)
                        continue
                else:
                    print("You have no Shield equipped")
                    input("")
                    continue
            case "4":
                # show current player stats
                print(f"Name --> {player.name}\nHP --> {player.hp}\nRaw Attack Bonus--> {player.attack_bonus}\nRaw Defence Bonus --> {player.defence_bonus}")
                input("")
                continue
            case _:
                print("Invalid action. Please choose 1, 2, 3.")
                continue
        # Enemy's turn if still alive
        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn:")
            enemy.attack(player)

    if player.is_alive():
        print(f"\nYou defeated the {enemy.name}!")
        enemy.drop(player) # after a basic enemy is killed, loot is dropped here
        input("")
    else:
        print("\nYou have been defeated.\nDeath is not the end...")
        input("")
        game_start()

def regular_enemy_combat_loop(player):
    i=1
    while True:
        clear_terminal()
        print("Combat will soon commence, would you like to craft something? Y/N")
        choice = input("")
        if choice in ("y", "Y"):
            crafting_menu(player)
        elif choice in ("n", "N"):
            if i < 5:
                # once i reaches 4, the regular enemy loop will stop.
                i+=1
                combat(player, enemy_picker(random.choice([1,2,3,4])))
            else:
                break
        else:
            print("Input error, please try again")
            input("")
            continue

def boss_combat_loop(player, boss):
    clear_terminal()
    print(f"\nA wild {boss.name} appears!")
    turn=0
    while player.is_alive() and boss.is_alive():
        turn += 1
        print(f"Turn: {turn}")
        if boss.check_turn(turn+1) == True:
            print("Turn limit reached. The Iron Doors close before you.")
            input("")
            return
        print(f"\n {boss.name} stands before you.")
        print(f"{boss.name} will cast you out in {boss.no_of_turns} turns.")
        # Player's turn
        print("\nYour turn:")
        print("1. Attack")
        print("2. Show Inventory")
        print("3. Defend")
        print("4. Current Stats")
        match input("Choose your action: "):
            # action depending on player choice
            case '1':
                # player chooses to attack
                true_false = []
                for i in player.equipped_items:
                    if isinstance(i, Weapon_Item): 
                        # if the item in the list is an object belonging to the Weapon_Item class, True is added to the true_false list
                        true_false.append(True)
                        item_damage = i.damage
                    else:
                        # if the item is anything else, False is added to the true_false list
                        true_false.append(False)
                if any(true_false):
                    print("Weapon Equipped.")
                else:
                    print("You have no weapon equipped")
                    item_damage = 0
                    continue
                player.attack(boss, item_damage)
            case '2':
                # interact with inventory
                inventory_menu(player)
                continue
            case '3':
                # player chooses to defend
                true_false = []
                for i in player.equipped_items:
                    if isinstance(i, Shield_Item): 
                        # if the item in the list is an object belonging to the Wshield_Item class, True is added to the true_false list
                        true_false.append(True)
                    else:
                        # if the item is anything else, False is added to the true_false list
                        true_false.append(False)
                if any(true_false):
                    # in other words, if a shield is equipped, the player has a chance to defend 
                    print("Shield Equipped.")
                    if random.random() < 0.5: # random.random() generates a random float between 0.0 and 1.0
                        print(f"{player.name} successfully defended!")
                        continue
                    else:
                        print(f"{player.name} couldn't defend!")                
                else:
                    print("You have no Shield equipped")
                    input("")
                    continue
            case "4":
                # show current player stats
                print(f"Name --> {player.name}\nHP --> {player.hp}\nRaw Attack Bonus--> {player.attack_bonus}\nRaw Defence Bonus --> {player.defence_bonus}")
                input("")
                continue
            case _:
                print("Invalid action. Please choose 1, 2, 3.")
                continue
        # Enemy's turn if still alive
        if boss.is_alive():
            if boss.check_turn(turn+1) == True:
                print("Max")
            else:
                print(f"\n{boss.name}'s turn:")
                boss.attackplayer(player)

    if player.is_alive():
        print(f"\nYou defeated the {boss.name}!")
        boss.drop(player) # after every basic enemy is killed, loot is dropped here
        input("")
    else:
        print("\nYou have been defeated.\nDeath is not the end...")
        input("")
        game_start()

def boss_rush(player):
    while True:
        boss_enemies = [
            Sapphire_Golem(),
            Bob_The_Assassin_King(),
            Slime_Queen(),
            Resurrected_Rubber_Ducky()
        ]
        current_boss = random.choice(boss_enemies)
        boss_enemies.remove(current_boss)
        boss_combat_loop(player, current_boss)


def game_start():
    # User decides their character's name
    clear_terminal()
    print("============== Dungeon Runner ==============\n")
    name = input("Enter your character's name: ")
    player = Character(name)
    # Add a simple starter item as an Item object
    loaded_inventory = load_data1()
    if loaded_inventory:
        for item in loaded_inventory:
            player.add_item(item)
            print(f"{item.name} added to inventory")
    input("")        
    loaded_equipped = load_data2()
    if loaded_equipped:
        for item in loaded_equipped:
            player.equipped_items.append(item)
            print(f"{item.name} added to equipped_items")
    input("")
    player.add_item(Weapon_Item("Wooden Sword", 20, "A basic wooden sword."))
    print(f"\nA wooden sword has been added to your inventory as using your bare hands from the beginning would be ineffective.\n")
    input("")
    while True:
        clear_terminal
        player.hp = 100 # at the beginning of each run health, any attack or defence bonus is reset to the default amount
        player.defence_bonus = 0
        player.attack_bonus = 0
        print("\n=== Main Menu ===")
        print("1. Normal Dungeon")
        print("2. Boss Rush")
        print("3. Quit")
        print("?  Help")
        choice = input("")
        if choice == "1":
            # starts normal dungeon game mode
            clear_terminal()
            print(f"{player.name} will now venture into the dungeon.")
            regular_enemy_combat_loop(player)
            input("")
            print(f"{player.name} stands before a large set of iron doors.")
            print("1. Craft")
            print("2. Proceed")
            choice = input("")
            if choice == "1": 
                crafting_menu(player)
            elif choice == "2":
                boss_combat_loop(player, boss_picker(random.choice([1,2,3,4])))
            else:
                print("Input Error")
                continue
        elif choice == "2":
            # starts boss gauntlet game mode
            print(f"{player.name} attempts the Boss Gauntlet.")
            input("")
            boss_rush(player)
        elif choice == "3":
            # write data to a file and exit the game
            dump_data(player.inventory, player.equipped_items)
            break
        elif choice == "?":
            # a simply explanation of the games various choices
            print("\nNormal Dungeon - Regular game mode which involves the player face four varying regular enemies, before a final boss confrontation.")
            print("Boss Rush - A game mode where you will face all dungeon bosses (and only the dungeon bosses) in succession.")
            input("")
        else:
            print("Invalid Input.")

def dump_data(dump_inventory, dump_equipped_items):
    with open('Game_Inventory.pkl', 'wb') as inventoryf:
        pickle.dump(dump_inventory, inventoryf)
    print("Inventory Saved")
    inventoryf.close()
    with open('Game_Equipped_Items.pkl', 'wb') as itemf:
        pickle.dump(dump_equipped_items, itemf)
    itemf.close
    print("Equipped Items Saved")
    return
#####################################################################################################################
def load_data1():
    # retrieves previous inventory items
    try:
        with open('Game_Inventory.pkl', 'rb') as f:
            loaded_file = pickle.load(f)
    except:
        print('No retrievable file with game inventory. Fresh inventory will be created.')
        return None
    f.close
    return loaded_file

def load_data2():
    # retrieves previously equipped items
    try:
        with open('Game_Equipped_Items.pkl', 'rb') as f:
            loaded_file = pickle.load(f)
    except:
        print("No retrievable file with Equipped Items. No starting equipped items.")
        return None
    f.close
    return loaded_file

if __name__ == "__main__":
    game_start()