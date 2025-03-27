
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
        return f"{self.name}: {self.description}" if self.description else self.name


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
    def __init__(self, name, hp=50):
        self.name = name
        self.hp = hp

    def is_alive(self):
        return self.hp > 0

    def attack(self, character):
        damage = random.randint(5, 10)
        print(f"{self.name} attacks {character.name} for {damage} damage!")
        character.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name} takes {damage} damage! (HP: {self.hp})")


class Goblin(Enemy):
    def __init__(self, name='Goblin', hp=50):
        super().__init__(name, hp)

class Slime(Enemy):
    def __init__(self, name='Slime', hp=50):
        super().__init__(name, hp)

class Golden_Unicorn(Enemy):
    def __init__(self, name='Golden Unicorn', hp=50):
        super().__init__(name, hp)

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

def main_menu():
    while True:
        print("\n=== RPG Starter Adventure ===")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter your character's name: ")
            player = Character(name)
            # Add a simple starter item as an Item object
            player.add_item(Item("Wooden Sword", "A basic wooden sword."))
            combat(player, Slime())
        elif choice == '2':
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
