
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
