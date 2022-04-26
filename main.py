# Want to make a loading screen thing
import intro
import mage
import monster
import barbarian
import hunter
import fight
import door
intro.intro_to_game()
player = intro.name_of_adventurer()
print(f"Ahhh a worthy name {player} \nworthy of the champion")
intro.intro_to_game_part_two(player)
# todo fix bad barbarian input.
# todo All if block need an else statement that forces the user back through.
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
# minotaur_attacks = monster.minotaur_attacks()[" "]
blob_health = monster.blob_stats()["blob_health"]
blob_dmg = monster.blob_stats()["blob_dmg"]
troll_name = monster.troll_stats()["name"]
minotaur_name = monster.minotaur_stats()["name"]
blob_name = monster.blob_stats()["name"]
# blob_attacks = monster.blob_attacks()[" "]
print("the hero's you can chose from are \n Barbarian \n Mage \n Hunter")
while True:
    hero = input("Please chose your hero\n")
    hero = hero.lower()
    if hero == "barbarian":
        print("You have chosen your hero")
        print("Here are your skills")
        print("To use your skills just type the name of the skill with a lowercase")
        print("Also when you come to a door please type your choice with lowercase")
        hero_stats = barbarian.hero_stats()
        hero_attacks = barbarian.hero_attacks()
        hero_buffs = barbarian.hero_buffs()
        hero_items = barbarian.hero_items()
        break
    elif hero == "mage":
        print("You have chosen mage")
        print("Here are your skills")
        print("To use your skills just type the name of the skill with a lowercase")
        print("Also when you come to a door please type your choice with lowercase")
        hero_stats = mage.hero_stats()
        hero_attacks = mage.hero_attacks()
        hero_buffs = mage.hero_buffs()
        hero_items = mage.hero_items()
        break
    elif hero == "hunter":
        print("You have chosen hunter")
        print("Here are your skills")
        print("To use your skills just type the name of the skill with a lowercase")
        print("Also when you come to a door please type your choice with lowercase")
        hero_stats = hunter.hero_stats()
        hero_attacks = hunter.hero_attacks()
        hero_buffs = hunter.hero_buffs()
        hero_items = hunter.hero_items()
        break
    else:
        print("you need to chose a hero\n Barbarian \n Mage \n Hunter")
monster_health = goblin_health
combat_health = hero_stats["health"]
hero_attacks = hero_attacks
hero_buffs = hero_buffs
monster_name = monster.goblin_stats()["name"]
vampire_name = monster.vampire_stats()["name"]
ghost_name = monster.ghost_stats()["name"]
counter = hero_items["health_potion"]["uses"]
# fight.fight(hero_stats, hero_items, hero_buffs, hero_attacks, goblin_dmg, goblin_health)
door_choice = door.two_doors()
if door_choice == "right":
    print("A quick tip to use your attack remember you must type the attack with a lowercase spelling")
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=goblin_dmg, monster_health=goblin_health, monster_name=goblin_name)

if door_choice == "left":
    print("A quick tip to use your attack remember you must type the attack with a lowercase spelling")
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=skeleton_dmg, monster_health=skeleton_health, monster_name=skeleton_name)
door_choice_two = door.two_doors()
if door_choice_two == "left":
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=troll_dmg, monster_health=troll_health, monster_name=troll_name)

if door_choice_two == "right":
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=ghost_dmg, monster_health=ghost_health, monster_name=ghost_name)
door_choice_three = door.two_doors()
if door_choice_three == "right":
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=minotaur_dmg, monster_health=troll_health, monster_name=troll_name)
if door_choice_three == "center":
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=vampire_dmg, monster_health=vampire_health, monster_name=vampire_name)

if door_choice_three == "left":
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=minotaur_dmg, monster_health=minotaur_health, monster_name=minotaur_name)

boss_door = door.boss_door()
if boss_door == "continue":
    fight.fight(hero_stats=hero_stats, hero_items=hero_items, hero_buffs=hero_buffs, hero_attacks=hero_attacks,
                monster_dmg=blob_dmg, monster_health=blob_health, monster_name=blob_name)
print(f"congratulations on your victory {player}")
exit()
