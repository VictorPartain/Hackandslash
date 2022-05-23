import os
import artwork_mentions
import hero_description
import intro
import loadingscreen
import mage
import monster
import barbarian
import hunter
import fight
import door
import monster_art
import hero_art
import ending
from time import sleep
import monster_description


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.02)
    print()


loadingscreen.loading_screen()
sleep(1)
os.system('cls')
intro.intro_to_game()
player = intro.name_of_adventurer()
os.system('cls')
slowprint(f"Oh-hh a worthy name, {player} \nworthy of the champion")
intro.intro_to_game_part_two(player)
intro.intro_three(player)
goblin_health = monster.goblin_stats()["goblin_health"]
goblin_name = monster.goblin_stats()["name"]
goblin_dmg = monster.goblin_stats()["goblin_dmg"]
skeleton_health = monster.skeleton_stats()["skeleton_health"]
skeleton_name = monster.skeleton_stats()["name"]
skeleton_dmg = monster.skeleton_stats()
skeleton_dmg = skeleton_dmg["skeleton_dmg"]
vampire_health = monster.vampire_stats()["vampire_health"]
vampire_dmg = monster.vampire_stats()["vampire_dmg"]
troll_health = monster.troll_stats()["troll_health"]
troll_dmg = monster.troll_stats()["troll_dmg"]
ghost_health = monster.ghost_stats()["ghost_health"]
ghost_dmg = monster.ghost_stats()["ghost_dmg"]
minotaur_health = monster.minotaur_stats()["minotaur_health"]
minotaur_dmg = monster.minotaur_stats()["minotaur_dmg"]
dragon_health = monster.dragon_stats()["dragon_health"]
dragon_dmg = monster.dragon_stats()["dragon_dmg"]
troll_name = monster.troll_stats()["name"]
minotaur_name = monster.minotaur_stats()["name"]
dragon_name = monster.dragon_stats()["name"]
vampire_name = monster.vampire_stats()["name"]
ghost_name = monster.ghost_stats()["name"]
print("\n Barbarian \n Mage \n Hunter")
while True:
    hero = input("Please chose your hero\n")
    hero = hero.lower()
    if hero == "barbarian":
        os.system('cls')
        hero_art.barbarian_art()
        hero_description.barbarian_story()
        os.system('cls')
        hero_stats = barbarian.hero_stats()
        hero_attacks = barbarian.hero_attacks()
        hero_items = barbarian.hero_items()
        slowprint("You have chosen your hero")
        slowprint("Here are your skills")
        slowprint(hero_attacks)
        slowprint(hero_items)
        slowprint("To use your skills just type the name of the skill")
        slowprint("Also when you stumble across a door please type your choice")
        os.system('cls')
        break
    elif hero == "mage":
        os.system('cls')
        hero_art.mage_art()
        hero_description.mage_story()
        os.system('cls')
        hero_stats = mage.hero_stats()
        hero_attacks = mage.hero_attacks()
        hero_items = mage.hero_items()
        slowprint("You have chosen mage")
        slowprint("Here are your skills")
        slowprint(hero_attacks)
        slowprint(hero_items)
        slowprint("To use your skills just type the name of the skill")
        slowprint("Also when you come to a door please type your choice")
        os.system('cls')
        break
    elif hero == "hunter":
        os.system('cls')
        hero_art.hunter_art()
        hero_description.hunter_story()
        os.system('cls')
        hero_stats = hunter.hero_stats()
        hero_attacks = hunter.hero_attacks()
        hero_items = hunter.hero_items()
        slowprint("You have chosen hunter")
        slowprint("Here are your skills")
        slowprint(hero_attacks)
        slowprint(hero_items)
        slowprint("To use your skills just type the name of the skill")
        slowprint("Also when you come to a door please type your choice")
        os.system('cls')
        break
    else:
        slowprint("you need to chose a hero\n Barbarian \n Mage \n Hunter")

counter = hero_items["health_potion"]["uses"]
os.system('cls')
door.two_door_art()
door_choice = door.two_doors()
door_choice.lower()
if door_choice == "right":
    os.system('cls')
    monster_description.goblin_description()
    monster_art.goblin_art()
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
                monster_dmg=goblin_dmg, monster_health=goblin_health, monster_name=goblin_name)
    sleep(1)
    os.system('cls')

if door_choice == "left":
    os.system('cls')
    monster_art.skeleton_art()
    monster_description.skeleton_description()
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
                monster_dmg=skeleton_dmg, monster_health=skeleton_health, monster_name=skeleton_name)
    sleep(1)
    os.system('cls')

# door.two_door_art()
# door_choice_two = door.two_doors()
# door_choice_two.lower()
# if door_choice_two == "left":
#     os.system('cls')
#     monster_art.troll_art()
#     monster_description.troll_description()
#     fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
#                 monster_dmg=troll_dmg, monster_health=troll_health, monster_name=troll_name)
#     sleep(1)
#     os.system('cls')
#
# if door_choice_two == "right":
#     os.system('cls')
#     monster_art.ghost_art()
#     monster_description.ghost_description()
#     fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
#                 monster_dmg=ghost_dmg, monster_health=ghost_health, monster_name=ghost_name)
#     sleep(1)
#     os.system('cls')

door.three_door_art()
door_choice_three = door.three_door()
door_choice_three.lower()
if door_choice_three == "right":
    os.system('cls')
    # add description of fight
    monster_art.minotaur_art()
    monster_description.minotaur_description()
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
                monster_dmg=minotaur_dmg, monster_health=troll_health, monster_name=troll_name)
    os.system('cls')
if door_choice_three == "center":
    os.system('cls')
    monster_art.vampire_art()
    monster_description.vampire_description()
    # add description of fight
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
                monster_dmg=vampire_dmg, monster_health=vampire_health, monster_name=vampire_name)
    os.system('cls')

if door_choice_three == "left":
    os.system('cls')
    monster_art.minotaur_art()
    monster_description.minotaur_description()
    # add description of fight
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
                monster_dmg=minotaur_dmg, monster_health=minotaur_health, monster_name=minotaur_name)
    os.system('cls')

door.boss_door_art()
boss_door = door.boss_door()
boss_door.lower()
if boss_door == "open":
    os.system('cls')
    monster_art.dragon_art()
    monster_description.dragon_description()
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
                monster_dmg=dragon_dmg, monster_health=dragon_health, monster_name=dragon_name)
loadingscreen.ending_scene()
# ending.ending_text(player)
artwork_mentions.artwork()

