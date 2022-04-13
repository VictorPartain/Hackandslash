import mage
import monster
import barbarian
import hunter

# todo fix bad barbarian input.
# todo All if block need an else statement that forces the user back through.
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
print("the hero's you can chose from are \n Barbarian \n Mage \n Hunter")

while True:
    hero = input("Please chose your hero\n")
    hero = hero.lower()
    if hero == "barbarian":
        print("You have chosen your hero")
        print("A goblin has appeared please use one of your skills")
        print("Here are your skills")
        hero_stats = barbarian.hero_stats()
        hero_attacks = barbarian.hero_attacks()
        hero_buffs = barbarian.hero_buffs()
        break
    elif hero == "mage":
        print("you have chosen mage")
        print("a goblin has appeared please use one of your skills")
        print("Here are your skills")
        hero_stats = mage.hero_stats()
        hero_attacks = mage.hero_attacks()
        hero_buffs = mage.hero_buffs()
        break
    elif hero == "hunter":
        print("you have chosen hunter")
        print("a goblin has appeared please use one of your skills")
        print("Here are your skills")
        hero_stats = hunter.hero_stats()
        hero_attacks = hunter.hero_attacks()
        hero_buffs = hunter.hero_buffs()
        break
    else:
        print("you need to chose a hero\n Barbarian \n Mage \n Hunter")

health = hero_stats["health"]
hero_attacks = hero_attacks
hero_buffs = hero_buffs

while not health <= 0:
    print(hero_attacks)
    print(hero_buffs)
    choice = input("please chose a skill form the list above\n")
    if choice in hero_buffs.keys():
        print(f"you used {choice}")
        health = health + hero_buffs[choice]
        print(health)
    if choice in hero_attacks.keys():
        goblin_health = goblin_health - hero_attacks[choice]
        health = health - goblin_dmg
        print(f"the goblin has {goblin_health} health remaining")
        print(f"you have {health} health remaining")
    else:
        health = health - goblin_dmg
        print(f"you have took{goblin_dmg}")

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

door = input("what door would you like to chose")
if door == "left":
    print("a skeleton emerges from the shadows")
    print("it is time to fight again")
    print(f"the skeleton has {skeleton_health} health  good luck hero")
    while not health <= 0:
        print(hero_attacks)
        choice = input(" ")
        if choice in hero_attacks.keys():
            skeleton_health = skeleton_health - hero_attacks[choice]
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
        print(hero_buffs)
        choice = input()
        if choice in hero_buffs.keys():
            health = health + hero_buffs[choice]
            health = health - skeleton_dmg
            print(f"you used {choice}")

        if choice in hero_attacks.keys():
            skeleton_health = skeleton_health - hero_attacks[choice]
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
else:
    print("that isn't an option")
# todo: This is broken logic in your if statement.

    door2 = input("you must choose another door adventurer \n left or right \n")
    if door2 == "right":
        print("a poltergeist appears from the floor")
        print("prepare your self brave hero")
        while not health <= 0:
            print(hero_attacks)
            choice = input(" ")
            if choice in hero_attacks.keys():
                poltergeist_health = poltergeist_health - hero_attacks[choice]
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
    # todo: adding spacing and new lines to have it read smoother
    # todo: Does it matter that the player knows about negative number of health or just they won?
    if door2 == "left":
        print("A troll is waiting for you prepared to attack")
        print("get ready to fight adventurer")
        while not health <= 0:
            print(hero_attacks)
            choice = input(" ")
            if choice in hero_attacks.keys():
                troll_health = troll_health - hero_attacks[choice]
                health = health - troll_dmg
                print(f"you have {health} health remaining")
                if troll_health < 0:
                    print("you have won")
                else:
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
    else:
        print("please chose a valid door they are \n right and left\n")

print("adventurer your fight is almost over now you must chose between 3 choices \n right, left, and center")
door3 = input("please choose your door\n")
if door3 == "right":
    print("hero you have chosen the wrong door \n you must now fight the minotaur in his own territory \n I wish you "
          "the best of luck adventurer,\n also the minotaur has its own unique skill be aware of "
          "this.")
    while not health <= 0:
        print(hero_attacks)
        choice = input(" ")
        if choice in hero_attacks.keys():
            minotaur_health = minotaur_health - hero_attacks[choice]
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
        choice = input(" ")
        if choice in hero_attacks.keys():
            minotaur_health = minotaur_health - hero_attacks[choice]
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
        choice = input(" ")
        if choice == "slash":
            vampire_health = vampire_health - hero_attacks[choice]
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
        choice = input(" ")
        if choice in hero_attacks.keys():
            blob_health = blob_health - hero_attacks[choice]
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

print("TEST")
