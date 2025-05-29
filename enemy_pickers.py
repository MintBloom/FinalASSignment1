
def enemy_picker(x):
    # depending on the value of x, an enemy is returned.
    list_of_enemies = {1:Slime, 2:Skeleton, 3:Goblin, 4:Golden_Unicorn}
    return list_of_enemies[x]

def boss_picker(x):
    # depending on the value of x, an enemy is returned.
    list_of_bosses = {1:Sapphire_Golem, 2:Slime_Queen, 3:Bob_The_Assassin_King, 4:Resurrected_Rubber_Ducky}
    return list_of_bosses[x]
