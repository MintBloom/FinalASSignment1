
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