import monster
from barbarian import hero_stats
from barbarian import hero_attacks
from barbarian import hero_buffs
# from mage import hero_attacks
# from mage import hero_stats
# from mage import hero_buffs
hero_stats = hero_stats()
hero_attacks = hero_attacks()
hero_buffs = hero_buffs()
health = hero_stats["barb_health"]
slash = hero_attacks["slash"]
enrage = hero_buffs["enrage"]
goblin_health = monster.goblin_stats()["goblin_health"]
goblin_dmg = monster.goblin_stats()["goblin_dmg"]
skeleton_health = monster.skeleton_stats()["skeleton_health"]
skeleton_dmg = monster.skeleton_stats()["skeleton_health"]
vampire_health = monster.vampire_stats()["vampire_health"]
vampire_dmg = monster.vampire_stats()["vampire_dmg"]
troll_health = monster.troll_stats()["troll_health"]
troll_dmg = monster.troll_stats()["troll_dmg"]
poltergeist_health = monster.poltergeist_stats()["poltergeist_health"]
poltergeist_dmg = monster.poltergeist_stats()["poltergeist_dmg"]
minotaur_health = monster.minotaur_stats()["minotaur_health"]
minotaur_dmg = monster.minotaur_stats()["minotaur_dmg"]
# minotaur_attacks = monster.minotaur_attacks()[" "]
blob_health = monster.blob_stats()["blob_health"]
blob_dmg = monster.blob_stats()["blob_dmg"]
# blob_attacks = monster.blob_attacks()[" "]
hero = input("Please chose your hero\n")
if hero == "Barbarian":
    print("You have chosen your hero")
    print("A goblin has appeared please use on of your skills")
    print("Here are your skills")

while not health <= 0:
    print(hero_attacks)
    attack = input(" ")
    if attack == "slash":
        goblin_health = goblin_health - slash
        health = health - goblin_dmg
        print(f"the goblin has {goblin_health} health remaining")
        print(f"you have {health} health remaining")

        # if attack == "2":
        #  print(f"your currant damage using slash is {slash}")
        #    print("The goblin has attacked you")
        #    barb_health = barb_health - goblin_dmg
        #    print(f"You have {barb_health} health remaining ")

        if health <= 0:
            print("you have died")
            exit()

        if goblin_health <= 0:
            print("you have won")
            break
door = input("Please chose a door left or right")

if door == "left":
    print("a skeleton emerges from the shadows")
    print("it is time to fight again")
    print(f"the skeleton has {skeleton_health} health remaining good luck hero")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            skeleton_health = skeleton_health - slash
            health = health - skeleton_dmg
            print(f"you have {health} health remaining")
            print(f"the skeleton has {skeleton_health} health remaining")
        else:
            print("there is no attacked named that")
            health = health - skeleton_dmg
            print(f"you took {skeleton_dmg} damage and have {health} health remaining")
        if health <= 0:
            print("you have died")
            exit()
        if skeleton_health <= 0:
            print("you have won")
            break

elif door == "right":
    print("it is time to fight again")
    print(" a skeleton emerges from the corner of the room")
    print(f"the skeleton has {skeleton_health} health remaining good luck hero")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            skeleton_health = skeleton_health - slash
            health = health - skeleton_dmg
            print(f"you have {health} health remaining")
            print(f"the skeleton has {skeleton_health} health remaining")
        else:
            print("there is no attacked named that")
            health = health - skeleton_dmg
            print(f"you took {skeleton_dmg} damage and have {health} health remaining")
        if health <= 0:
            print("you have died")
            exit()
        if skeleton_health <= 0:
            print("you have won")
            break

door2 = input("you must choose another door adventurer")
if door2 == "right":
    print("a poltergeist appears from the floor")
    print("prepare your self brave hero")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            poltergeist_health = poltergeist_health - slash
            health = health - poltergeist_dmg
            print(f"you have {health} health remaining")
            print(f"the troll has {poltergeist_health} remaining")
        else:
            print("there is not an attack named that")
            health = health - poltergeist_dmg
            print(f"you have taken{poltergeist_dmg} you have {health} remaining")
        if health <= 0:
            print("you have died")
            exit()
        if troll_health <= 0:
            print("you have won")
            break

if door2 == "left":
    print("A troll is waiting for you prepared to attack")
    print("get ready to fight adventurer")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            troll_health = troll_health - slash
            health = health - troll_dmg
            print(f"you have {health} health remaining")
            print(f"the troll has {troll_health} remaining")
        else:
            print("there is not attacked named that")
            health = health - troll_dmg
            print(f"you took {troll_dmg} damage and have {health} health remaining")
        if health <= 0:
            print("you have died")
            exit()
        if troll_health <= 0:
            print("you have won")
            break

print("adventurer your fight is almost over now you must chose between 3 choices \n right, left, and center")
door3 = input("please choose your door")
if door3 == "right":
    print("hero you have chosen the wrong door \n you must now fight the minotaur in his own territory \n I wish you "
          "the best of luck adventurer,\n also the minotaur has its own unique skill be aware of "
          "this.")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            minotaur_health = minotaur_health - slash
            health = health - minotaur_dmg
            print(f"hero you have {health} health remaining")
            print(f"the minotaur has {minotaur_health} health remaining")
            print("continue fighting brave adventurer")
        else:
            print("there is no attacked named that")
            health = health - minotaur_dmg
            print(f"you took {minotaur_dmg} damage and have {health} health remaining")
        if health <= 0:
            print("you have died")
            exit()
        if minotaur_health <= 0:
            print("you have triumphed")
            exit()
if door3 == "left":
    print("hero you have chosen the wrong door \n you must now fight the minotaur in his own territory \n I wish you "
          "the best of luck adventurer,\n also the minotaur has its own unique skill be aware of "
          "this.")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            minotaur_health = minotaur_health - slash
            health = health - minotaur_dmg
            print(f"hero you have {health} health remaining")
            print(f"the minotaur has {minotaur_health} health remaining")
            print("continue fighting brave adventurer")
        else:
            print("there is no attacked named that")
            health = health - minotaur_dmg
            print(f"you took {minotaur_dmg} damage and have {health} health remaining")
        if health <= 0:
            print("you have died")
            exit()
        if minotaur_health <= 0:
            print("you have triumphed")
            exit()

# still a work in progress
if door3 == "center":
    print("a vampire falls from the ceiling staring at you")
    print("brace yourself adventurer and get ready for a fight")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            vampire_health = vampire_health - slash
            health = health - vampire_dmg
            print(f"you have {health} health remaining")
            print(f"the vampire has {vampire_health} health remaining")
        else:
            print("there is no attacked named that")
            health = health - vampire_dmg
            print(f"you took {vampire_dmg} damage and have {health} health remaining")
        if health <= 0:
            print("you have died")
            exit()
        if vampire_health <= 0:
            print("you have won")
            break
print("there is only one door remaining please type continue")
boss_door = input(" ")
if boss_door == "continue":
    print("a giant blob is in the center of the room get prepared adventurer")
    print("the boss has awakened")
    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            blob_health = blob_health - slash
            health = health - blob_dmg
            print(f"you have {health} health remaining hero you got this")
            print(f"the blob has {blob_health} health remaining")
        else:
            print(f"hero there isn't an attacked named that")
            health = health - blob_dmg
            print(f"you took {blob_dmg} and have {health} health remaining")
        if health <= 0:
            print("you have died hero")
            exit()
        if blob_health <= 0:
            print("you have won")
            print("Congratulations on your victory")
            exit()
