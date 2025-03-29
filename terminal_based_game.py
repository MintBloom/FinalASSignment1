
# main to dos:
# enhance combat system
# items stats with combat loop
# introduce drops
# implement consumables
# expand inventory and introduce crafting
# save/load functionality

# to dos for code presentation:
# implement unit tests
# high quality coding standards
# documentation via. README and comments



import random

class Item:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def __str__(self):
        # returns an item's name and it's description
        return f"{self.name}: {self.description}" if self.description else self.name
    
class Weapon_Item(Item):
    def __init__(self, name, description=""):
        super().__init__(name, description)
    
class Stat_Boost_Item(Item):
    def __init__(self, name, description=""):
        super().__init__(name, description)

class Health_Items(Item):
    def __init__(self, name, description=""):
        super().__init__(name, description)


class Character:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.inventory = []  # Inventory holds Item objects in this list

    def is_alive(self):
        return self.hp > 0

    def attack(self, enemy):
        damage = random.randint(5, 15)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("Inventory:")
        if not self.inventory:
            print("  (empty)")
        else:
            for item in self.inventory:
                print(f"  - {item}")


class Enemy:
    def __init__(self, name, min_dmg, max_dmg, hp=50):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def attack(self, character):
        damage = random.randint(self.min_dmg, self.max_dmg)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        character.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")

class Slime(Enemy):
    def __init__(self, name="Slime", min_dmg=5, max_dmg=10, hp=50):
        super().__init__(name, min_dmg, max_dmg, hp)

class Goblin(Enemy):
    def __init__(self, name="Goblin", min_dmg=9, max_dmg=16, hp=50):
        super().__init__(name, min_dmg, max_dmg, hp)

class Golden_Unicorn(Enemy):
    def __init__(self, name="Golden Unicorn", min_dmg=15, max_dmg=24, hp=50):
        super().__init__(name, min_dmg, max_dmg, hp)

def combat(player, enemy):
    print(f"\nA wild {enemy.name} appears!")
    while player.is_alive() and enemy.is_alive():
        # Player's turn
        print("\nYour turn:")
        print("1. Attack")
        print("2. Show Inventory")
        print("3. Flee")
        action = input("Choose your action: ")

        # action depending on player choice
        if action == '1':
            player.attack(enemy)
        elif action == '2':
            player.show_inventory()
            continue  # Skip enemy turn to allow further action after checking inventory.
        elif action == '3':
            if random.random() < 0.5: # random.random() generates a random number between 0-1
                print("You successfully fled!")
                return
            else:
                print("Failed to flee!")
        else:
            print("Invalid action. Please choose 1, 2, or 3.")
            continue

        # Enemy's turn if still alive
        if enemy.is_alive():
            print(f"\n{enemy.name}'s turn:")
            enemy.attack(player)

    if player.is_alive():
        print(f"\nYou defeated the {enemy.name}!")
    else:
        print("\nYou have been defeated.")

def consumable_menu():
    pass

def crafting_menu():
    pass

def enemy_picker(x):
    # depending on the value of x, an enemy is returned. Slime is most likely to be returned, then Goblin, and the Golden Unicorn is least likely 
    if 0.0 <= x <= 0.5:
        return Slime()
    elif 0.51 <= x <= 0.8:
        return Goblin()
    elif 0.81 <= x <= 1:
        return Golden_Unicorn()

def main_menu():
    # main menu or "start" of the game
    while True:
        print("\n=== RPG Starter Adventure ===")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            # User decides their character's name
            name = input("Enter your character's name: ")
            player = Character(name)
            # Add a simple starter item as an Item object
            player.add_item(Item("Wooden Sword", "A basic wooden sword."))
            print(f"A wooden sword has been added to your inventory as using your bare hands from the beginning would be ineffective.\nNow you can defend yourself.")
            while True:
                print(f"What would you {player} like to do?")
                print("1. Craft")
                print("2. Venture into combat")
                print("3. Random Drop Chance")
                action = input("")
                if action == "1":
                    crafting_menu()
                elif action == "2":
                    combat(player, enemy_picker(random.random()))
                elif action == "3":
                    continue
                else:
                    print("Invalid choice.")
        elif choice == '2':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
