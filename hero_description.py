from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.02)
    print()


def barbarian_story():
    slowprint("The Barbarian is a hero who relies on their brute strength and their two handed sword,\n"
              "Barbarians tend to be enormous, muscular and unshaven with little armor,\n"
              "this is because barbarians don't rely on armor they rely on their pure rage to continue fighting\n"
              "Barbarians wont stop attacking until their limbs are utterly destroyed\n"
              "they have been known though out history to be one of the strongest and scariest warriors to exist\n"
              "because of this they are commonly seen in gladiator fights")


def mage_story():
    slowprint("The Mage is a hero who uses their wits and magical affinity to cast spells of mass destruction,\n"
              "mages wield a large staff and a grimoire although it is quite rare to see one, \n"
              "this is because of how much training and magical affinity it takes to become one \n"
              "they also tend to not wear much armor because it gets in the way of their spells so, they use a cloak")


def hunter_story():
    slowprint("The Hunter is a hero who uses their reflexes and accuracy to fel their foes,\n"
              "The Hunters tend to be some of the greatest assassins in the world,\n"
              "welding their long bow they can accurately shoot over 150 yards \n "
              "hunters tend to not wear much armor other than chainmail for minimal protection\n"
              "this is because it affects their accuracy and speed in a fight as well as how loud they are")
