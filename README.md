# Game Documentation

## Overview
This game is intended to be played through multiple times allowing for the use of various items and equipment. The core gameplay revolves around the player fighting four simple enemies and a big boss enemy at the end. The player may craft items outside of combat i.e. in between enemies and before a boss fight. There are four different basic enemies and four different boss enemies, each dropping various items and equipment. Whenever the player completes a run, their health will be reset to the base amount (100 HP) but they will be able to any previous items of armour they have collected. Likewise, when the player quits the game, everything in their inventory and equipped items will be saved, but nothing else.

## Combat System
In the game there are four different basic enemies: Slime, Goblin, Skeleton, Soldier and Golden Unicorn. There are also four main bosses in the game: Slime Queen, Sappire Golem, Bob the Assassin King and Resurrected Rubber Ducky. The basic enemies only differ in their respective lootpools and slightly varying health and attack power. The boss enemies also vary in the same way but have "wipe" mechanic, in which, after a certain amount of turns, the player will be kicked out (returning to the "start of the game" if the boss has not been defeated by then). I was planning on giving each boss a respective quirk, a dodge or enrage mechanic for example.
<br> During combat the player has a few different options; attack, block or view your inventory (which will enable further options such as equipping or unequipping an item or consuming an item).


## Item Statistics and Combat Loop
The items in the game can only effect two actual stats other than health, those being extra attack and/or defence bonuses. Any of these attack or defence bonuses are simply added to the player's respective attack or defence bonus.

#### Challenges
- Integrating Consumable Attack/Defence
The problem here was how to increase the attack or defence of the player without changing the actual weapon's damage, and so that the sttack or defence can be changed later if need be. To solve this I simply created extra Character.defence_bonus and Character.attack_bonus attributes which could be freely modified depending on other game effects, and would be added to the players overall damage or defence during combat. These attack and defence bonuses are also reset to zero at a the beginning of each run to help mitigate the player from becoming too strong too quickly.


## Item Drops
All items in the game (equipment, crafting ingredients, independant bonuses) can only be obtained via. enemy drops. The drops are randomised and each enemy in the game has a slightly different lootpool, although they do share some commonalities to try and keep the game fair, each enemy in the game drops some sort of health item for example. This way the player should be able to heal most of the time (although you can get an unlucky run with no health drops). However, the player is unable to pick and choose what they wish to loot - simply everything dropped will be added to the players inventory.


## Consumables
In the game there are various consumables that each do one or more of the following: increase health, increase damage or increase defence. Items that increase damage require you to have a weapon equipped and those that increase defence require you too have a shield equipped. There is no limit to how many items you can consume in a turn, however typically the player will not be in possession of a lot of items at once.

## Expand Inventory and Crafting
The inventory looks quite bare and simply shows all items in the order which they were looted from enemies. However when the player wants to craft or equip an item, they are show different menus, which only include equippable weapons or items to be used for crafting respectively. 

## Save/Load Functionality
Upon choosing the quit option in the main game menu the player's inventory and equipped items will be written, as a list, to separate, corresponding .pkl files using the built-in python pickle function. When loading into the game again, each of these files will be read or "unpickled" and each item will in turn be added to the inventory or equipped item (wherever it was originally pulled from).
#### Challenges
- Saving vs Game Balance
Since my game is designed to be replayed multiple times where the character is reset at the beginning of every playthrough, I was not originally intending to save anything at all, however that nets me no marks unfortunately. Now I have made it so that inventory and equipped items are saved if a player quits between playthroughs. This does mean unfortunately that anything the player has obtained from the previous playthroughs will be carried into future ones, introducing an innate inbalance to the game.

## Unit Testing
I do not have functional unit testing implemented for this project.
#### Challenges
- Implementing Unit Tests
Implementing unit tests was far more work than I had originally anticipated. Before searching up how to do more advanced unit tests (testing functions which require classes and other prerequisites to work) I assumed the tests would be as simple as in the practical session 6. After delving deeper I found that many tests I would have needed required "mock classes" which would, at the time, have taken me too long to implement as I had looked into this quite late.

## Code Quality
The various functions and classes have been commented on to explain what they do, and I have split up different tasks the code has to do into as many functions as I thought was appropriate. However, all the code is in a single file which is not very easy to read and having to scroll around during editing is an annoyance. There are certain parts of my game which were very inelegantly coded; for example the crafting menu and the main game menu. 
#### Challenges
- Code Across Files
In the end I decided to just leave all my code in one file as I have never split my code across several files, and without unittesting I decided that debugging my code would likely be more difficult. Most of the forums on Stack Overflow had a general consus that using several files and importing everything into one file, using the specific command import *(which imports everything into the chosen file), was not good practice. Supposedly using import * not recommended for the same reasons as global variables - it is difficult to keep track of all the possible interactions happening in the code, which can lead to unexpected bugs. 