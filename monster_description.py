from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.06)
    print()


def goblin_description():
    slowprint("A goblin is laying on the floor in front of you,\n"
              "the goblin is sickly green, it has tiny razor sharp fangs, and is about 3 feet tall\n"
              "goblins are known to be vicious foes when in a large pack\n"
              "luckily for you there is only one\n"
              "The goblin seems to be angered by your intrusion of its domain\n"
              "get ready to fight")


def skeleton_description():
    slowprint("You walk through the door to see a skeleton waiting for you,\n"
              "The skeleton is a common monster,\n"
              "They are mostly seen in graveyards or in dungeons,\n"
              "This skeleton is wielding an axe and a shield\n"
              "The skeleton rushes at you preparing to strike")


def troll_description():
    slowprint("As you walk into the door you see a troll sleeping\n"
              "the troll has a large nose and is covered with moss\n"
              "you suspect that the troll is at least four times your height\n"
              "you take the time to look around at your surroundings\n"
              "you see that you are in a large cavern,\n"
              "as you are looking around, the door you came from slams shut awaking the troll\n"
              "The troll seems to be very hungry, and wants to make you its dinner\n")


def vampire_description():
    slowprint("You walk into a dark and gloomy cavern and see a large coffin in the middle of the room,\n"
              "The coffin is surrounded by a pool of blood and you see bones in the corners of the room \n"
              "you suspect that there is a vampire in the coffin and prepare to fight\n"
              "as you walk towards the coffin the vampire launches itself into the air\n"
              "The vampire is dressed in an all black victorian suit with a black and red cape\n"
              "The vampire's fangs are large and sharp \n"
              "the vampire is preparing to feast on your body")


def ghost_description():
    slowprint("You open the door to see a ghost aimlessly floating around in a plain room,\n"
              "the ghost is a transparent white you see the ghost smack into a "
              "wall while seemingly looking for something\n"
              "you then notice that the ghost has spotted you and is preparing to attack you")


def dragon_description():
    slowprint("you open the final door and you see a large hoard of gold,\n"
              "you sense movement in the pile of gold and then you notice a large eye,\n"
              "the creature lifts it's self from the pile of gold to revel that it's a dragon,\n"
              "the dragon has scales the color of blood and fangs that are twice the size of your sword\n"
              "you need to quickly kill the dragon before it kills you and escapes")


def minotaur_description():
    slowprint("you open the door to a horrific sight,\n"
              "a long time ago you were told of a story about the infamous scandal of pasiphae,"
              "and how she gave birth to a half-human,half-bull monster of a son\n"
              "you never believed that story until now, in front of you was the minotaur sitting "
              "down waiting to attack you as it grabs its Ω shaped axe\n"
              "you notice that a horn was missing as you tried to recall how it went missing the minotaur attacks you")
