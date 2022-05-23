from time import sleep
import os


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.01)
    print()


def intro_three(player):
    slowprint(f"Hello {player}\n I know that you are feeling courageous but before you begin your adventure,\n I would"
              f"like to tell you the story of this land. \n In the kingdom of Audia there has existed pantheons of "
              f"gods and monsters. \nUnlike the Gods and monsters of your world there is not good Gods or monsters,"
              f"The Gods, Goddesses and monsters of this world only seek to destroy anyone who dares to become The "
              f"Champion\n You must be wondering what is the Champion, well The Champion is short for The Champion of"
              f"mankind.\n There have been many Champions before you, some could lift mountains with a single thought,\n"
              f"while others were gifted in brute strength and could punch a whole through an active Volcano.\n Although"
              f"these champions were mighty, \n They never achieved their goal, which was to kill all of the pantheons\n"
              f"That {player} is where you come in.\n I personally shall train you to become the Ultimate Champion.\n So"
              f"that even the gods will tremble before your power but first we must train you. I already found a dungeon"
              f"\nLets see what you can do hero")


def intro_to_game():
    slowprint("Hello Adventurer, \nI welcome you to a story \na story of The Champion")
    slowprint("But before we begin I must ask you a few questions \n"
              "my first request is that you tell me your name adventurer")


def name_of_adventurer():
    player = input("Please type your name below \n")
    return player


def intro_to_game_part_two(player):
    slowprint(f"I am glad that you joined us {player}")
    slowprint("Now that I know your name we must begin your adventure, \nThere is only one more "
              "step needed to continue and that is to chose your hero")
    slowprint("To chose your hero please type one of the three options")


def goblin_stats():
    return {
        "goblin_health": 7,
        "goblin_dmg": 10,
        "name": "goblin"
    }


def troll_stats():
    return {
        "troll_health": 150,
        "troll_dmg": 30,
        "name": "troll"
    }


def ghost_stats():
    return {
        "ghost_health": 200,
        "ghost_dmg": 30,
        "name": "ghost"
    }


def skeleton_stats():
    return {
        "skeleton_health": 80,
        "skeleton_dmg": 20,
        "name": "skeleton"
    }


def vampire_stats():
    return {
        "vampire_dmg": 40,
        "vampire_health": 200,
        "name": "vampire"
    }


def dragon_stats():
    return {
        "dragon_dmg": 15,
        "dragon_health": 500,
        "name": "dragon"
    }


def minotaur_stats():
    return {
        "minotaur_health": 400,
        "minotaur_dmg": 20,
        "name": "minotaur"
    }


def barb_stats():
    return {
        "dmg": 200,
        "health": 500,
        "defense": 30,
    }


def barb_attacks():
    return {
        "slash": 100
    }


def barb_items():
    return {
        "health_potion": {
            "potion_heal": 30,
            "uses": 3,
        }
    }


def two_doors():
    door = input("Choose a door \n left or right \n")
    door = door.lower()
    while True:
        if door == "left":
            return door

        if door == "right":
            return door
        else:
            slowprint("you have not chosen a valid door, please pick a valid door")
            door = input("Choose a door \n left or right \n")


def three_door():
    door = input("Choose a door \n left, right or center \n")
    door = door.lower()
    while True:
        if door == "left":
            return door

        if door == "right":
            return door

        if door == "center":
            return door
        else:
            slowprint("you have not chosen a valid door, please pick a valid door")
            door = input("Choose a door \n left, right or center \n")


def boss_door():
    door = input("there is only one door remaining, \n please type open to continue to the boss \n")
    door = door.lower()
    while True:
        if door == "open":
            return door
        else:
            slowprint("you did not choose a valid door, please try again")
            door = input("there is only one door remaining, \n please type open to continue to the boss \n")


def two_door_art():
    print(r"""
     ______                              ______
   ,-' ;  ! `-.                       ,-' ;  ! `-.                     
  / :  !  :  . \                     / :  !  :  . \
 |_ ;   __:  ;  |                   |_ ;   __:  ;  |
 )| .  :)(.  !  |                   )| .  :)(.  !  |
 |"    (##)  _  |                   |"    (##)  _  |
 |  :  ;`'  (_) (                   |  :  ;`'  (_) (
 |  :  :  .     |                   |  :  :  .     |
 )_ !  ,  ;  ;  |                   )_ !  ,  ;  ;  |
 || .  .  :  :  |                   || .  .  :  :  |
 |" .  |  :  .  |                   || .  .  :  :  |
 |mt-2_;----.___|                   || .  .  :  :  |

    """)


def three_door_art():
    print(r"""
     ______                              ______                           ______        
   ,-' ;  ! `-.                       ,-' ;  ! `-.                     ,-' ;  ! `-.           
  / :  !  :  . \                     / :  !  :  . \                   / :  !  :  . \             
 |_ ;   __:  ;  |                   |_ ;   __:  ;  |                 |_ ;   __:  ;  |              
 )| .  :)(.  !  |                   )| .  :)(.  !  |                 )| .  :)(.  !  |              
 |"    (##)  _  |                   |"    (##)  _  |                 |"    (##)  _  |             
 |  :  ;`'  (_) (                   |  :  ;`'  (_) (                 |  :  ;`'  (_) (              
 |  :  :  .     |                   |  :  :  .     |                 |  :  :  .     |              
 )_ !  ,  ;  ;  |                   |  :  :  .     |                 |  :  :  .     |           
 || .  .  :  :  |                   || .  .  :  :  |                 || .  .  :  :  |              
 |" .  |  :  .  |                   || .  .  :  :  |                 || .  .  :  :  |            
 |mt-2_;----.___|                   || .  .  :  :  |                 || .  .  :  :  |            
    """)


def boss_door_art():
    print(r"""
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
    """)


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


def barbarian_art():
    print(r"""

                                  á▄▓
                                  ▐██
                                  ▐▓▒
                                    ▓@    ▄▓▓▓▄
                                    ▓▓   ▓██████
                                    █▓█▄▄██▓▓██▓
                                    ███▓████▓▓╣██▓▓▓▄
                                ▄████▓████████▓▓▓▓▓▓██▄
                              ╓██▓▓▓██▓███████████▓██▓▓███▄
                             ▄███████▓█████▓▓▓▓▓▓▓▓███▓▓▓██▌
                            █████████████████▓▓▓▓▓▓▓███▓▓▓██▌
                           ▐███████████████████▓▓▓▓▓▓████▓▓██
                           ████████▓▓████████████▓▓██▓▓██████▌
                           ███████████████████████▓███▓███████
                          ▐████████████████▓████████████▓▓████
                          ████▓▓▓█████████████████▓██▓███▓███▌▌
                         ▐████▓▓▓███████████████▓█▓▓██████▓███
                         █████▓▓███████████████▓▓█▓▓██████████w
                         ████▓╣▓████████████████▓███▓█████▓████
                        ▐████▓▓▓█████████████████████▓████▓████▌
                        █████▓╢╢▓▓███████████████████▓▓█████████
                        █████▓▓▓▓█████████████████████▓▓████████▌  
                       ▐█████████████████████████████████████████
                       ▐█████████████████████████████████████████▌
                       ███████████████████████████████████████████U
                       ████████████████████████████████████████████
                      ▐████████████████████████████████▓███████████
                      █████████████████████████████████████████████▌
                     ▐█████████░████████████████████████▓▓██▌▀▀▀████
                    ▐█████████▌j██▓▓▓▓▓█████████░██▐█▓▓▓▓▓▓▀    ▀'`
                   j██▀ ▀▐███╙╒██▓▓▓▓▓▀▐███████▌ ▀▀▀████▓▓`
                   ▐░▀    ▀▀`   ████▀▀  ███████      ╙███▌
                   ▌      ░    ]██▓▌     ▀███▀        ████▄,            
                               ████        ▀▀  ,      ███████▄▄
                             ▓██▓▓                 ╜╜╜▀▀▀▀████
                            ▓███▓▌



    """)


def hunter_art():
    print(r"""

                                                       |
                                                        \.
                                                        /|.
                                                      /  `|.
                                                    /     |.
                                                  /       |.
                                                /         `|.
                                              /            |.
                                            /              |.
                                          /                |.
     __                                 /                  `|.
      -\                              /                     |.
        \\                          /                       |.
          \\                      /                         |.
           \|                   /                           |\
             \#####\          /                             ||
         ==###########>     /                               ||
          \##==      \    /                                 ||
     ______ =       =|__/___                                ||
 ,--' ,----`-,__ ___/'  --,-`-==============================##==========>
\               '        ##_______ ______   ______,--,____,=##,__
 `,    __==    ___,-,__,--'#'  ==='      `-'              | ##,-/
   `-,____,---'       \####\              |        ____,--\_##,/
       #_              |##   \  _____,---==,__,---'         ##
        #              ]===--==\                            ||
        #,             ]         \                          ||
         #_            |           \                        ||
          ##_       __/'             \                      ||
           ####='     |                \                    |/
            ###       |                  \                  |.
            ##       _'                    \                |.
           ###=======]                       \              |.
          ///        |                         \           ,|.
          //         |                           \         |.
                                                   \      ,|.
                                                     \    |.
                                                       \  |.
                                                         \|.
                                                         /.
                                                        |
    """)


def mage_art():
    print(r"""
                                  ....
                                .'' .'''
.                             .'   :
\\                          .:    :
 \\                        _:    :       ..----.._
  \\                    .:::.....:::.. .'         ''.
   \\                 .'  #-. .-######'     #        '.
    \\                 '.##'/ ' ################       :
     \\                  #####################         :
      \\               ..##.-.#### .''''###'.._        :
       \\             :--:########:            '.    .' :
        \\..__...--.. :--:#######.'   '.         '.     :
        :     :  : : '':'-:'':'::        .         '.  .'
        '---'''..: :    ':    '..'''.      '.        :'
           \\  :: : :     '      ''''''.     '.      .:
            \\ ::  : :     '            '.      '      :
             \\::   : :           ....' ..:       '     '.
              \\::  : :    .....####\\ .~~.:.             :
               \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
                \\    .'  ########## \ \ _.' '. '-.       '''.
                :\\  :     ########   \ \      '.  '-.        :
               :  \\'    '   #### :    \ \      :.    '-.      :
              :  .'\\   :'  :     :     \ \       :      '-.    :
             : .'  .\\  '  :      :     :\ \       :        '.   :
             ::   :  \\'  :.      :     : \ \      :          '. :
             ::. :    \\  : :      :    ;  \ \     :           '.:
              : ':    '\\ :  :     :     :  \:\     :        ..'
                 :    ' \\ :        :     ;  \|      :   .'''
                 '.   '  \\:                         :.''
                  .:..... \\:       :            ..''
                 '._____|'.\\......'''''''.:..'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)


def ending_text(player):
    slowprint(f"Congratulations on your victory {player}")
    slowprint("You should be very proud of your self, you have done what many have not")
    slowprint(f"This is the end for now {player} \nI hope to see you again in the next dungeon")


def death():
    print(r"""
                            ...
                          ;::::;
                        ;::::; :;
                     ;:::::'     :;
                     ;:::::;      ;.
                     ,:::::'      ;             OOO\
                    ::::::;       ;             OOOOO\
                    ;:::::;       ;             OOOOOOOO
                  ,;::::::;      ;'             / OOOOOOO
                 ;:::::::::`. ,,,;.           /  /DOOOOOO
                .';:::::::::::::::::;,       /  /   DOOOO
                ,::::::;::::::;;;;::::;,    /  /      DOOO
                ;`::::::`'::::::;;;::::: ,#/  /        DOOO
                :`:::::::`;::::::;;::: ;::#  /          DOOO
                ::`:::::::`;:::::::: ;::::# /            DOO
                `:`:::::::`;:::::: ;::::::#/             DOO
                :::`:::::::`;; ;:::::::::##               OO
                ::::`:::::::`;::::::::;:::#               OO
                `:::::`::::::::::::;'`:;::#               O
                `:::::`::::::::;' /  / `:#
                ::::::`:::::;'  /  /   `#
_____.___.________    ____ ___    ___ ___                              .___.__             .___ 
\__  |   |\_____  \  |    |   \  /   |   \ _____   ___  __  ____     __| _/|__|  ____    __| _/ 
 /   |   | /   |   \ |    |   / /    ~    \\__  \  \  \/ /_/ __ \   / __ | |  |_/ __ \  / __ |  
 \____   |/    |    \|    |  /  \    Y    / / __ \_ \   / \  ___/  / /_/ | |  |\  ___/ / /_/ |  
 / ______|\_______  /|______/    \___|_  / (____  /  \_/   \___  > \____ | |__| \___  >\____ |  
 \/               \/                   \/       \/             \/       \/          \/      \/  

    """)


def hunt_stats():
    return {
        "dmg": 200,
        "health": 100
    }


def hunt_attacks():
    return {
        "quickshot": 200
    }


def hunt_items():
    return {
        "health_potion": {
            "potion_heal": 30,
            "uses": 3,
        }
    }


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


def loading_screen():
    print(r"""

  ___ ___                   __                         .___         .__                   .__     
 /   |   \ _____     ____  |  | __ _____     ____    __| _/   ______|  |  _____     ______|  |__  
/    ~    \\__  \  _/ ___\ |  |/ / \__  \   /    \  / __ |   /  ___/|  |  \__  \   /  ___/|  |  \ 
\    Y    / / __ \_\  \___ |    <   / __ \_|   |  \/ /_/ |   \___ \ |  |__ / __ \_ \___ \ |   Y  \
 \___|_  / (____  / \___  >|__|_ \ (____  /|___|  /\____ |  /____  >|____/(____  //____  >|___|  /
       \/       \/      \/      \/      \/      \/      \/       \/            \/      \/      \/ 
    """)


def ending_scene():
    print(r"""
_________                                             __          .__             __.   __                         ._.
\_   ___ \   ____    ____     ____  _______ _____   _/  |_  __ __ |  |  _____   _/  |_ |__|  ____    ____    ______| |
/    \  \/  /  _ \  /    \   / ___\ \_  __ \\__  \  \   __\|  |  \|  |  \__  \  \   __\|  | /  _ \  /    \  /  ___/| |
\     \____(  <_> )|   |  \ / /_/  > |  | \/ / __ \_ |  |  |  |  /|  |__ / __ \_ |  |  |  |(  <_> )|   |  \ \___ \  \|
 \______  / \____/ |___|  / \___  /  |__|   (____  / |__|  |____/ |____/(____  / |__|  |__| \____/ |___|  //____  > __
        \/              \/ /_____/               \/                          \/                         \/      \/  \/
    """)


def mage_stats():
    return {
        "health": 50,
        "dmg": 300
    }


def mage_attacks():
    return {
        "fireball": 300
    }


def mage_items():
    return {
        "health_potion": {
            "potion_heal": 30,
            "uses": 3,
        }
    }


def goblin_art():
    print(r"""
             ,      ,
            /(.-""-.)\
        |\  \/      \/  /|
        | \ / =.  .= \ / |
        \( \   o\/o   / )/
         \_, '-/  \-' ,_/
           /   \__/   \
           \ \__/\__/ /
         ___\ \|--|/ /___
       /`    \      /    `\
      /       '----'       \

    """)


def troll_art():
    print(r"""
        -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \  \ |  /   _.' `_
    .-. \  `  || |  .' _.-' `.
  .' _ \ '  -    -'  - ` _.-.
   .' `. %%%%%   | %%%%% _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\#)\    (.(_).)    /(#//\
 ' / ) ((  /   | |   \  )) (`.`.
 .'  (.) \ .md88o88bm. / (.) \)
   / /| / \ `Y88888Y' / \ | \ \
 .' / O  / `.   -   .' \  O \ \\
  / /(O)/ /| `.___.' | \\(O) \
   / / / / |  |   |  |\  \  \ \
   / / // /|  |   |  |  \  \ \  
 _.--/--/'( ) ) ( ) ) )`\-\-\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
    """)


def skeleton_art():
    print(r"""
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
                             )(  l\ o ('..-.
                       _..--' _'-' '--'.-. |
                __,,-'' _,,-''            \ \
               f'. _,,-'                   \ \
              ()--  |                       \ \
                \.  |                       /  \
                  \ \                      |._  |
                   \ \                     |  ()|
                    \ \                     \  /
                     ) `-.                   | |
                    // .__)                  | |
                 _.//7'                      | |
               '---'                         j_| `
                                            (| |
                                             |  \
                                             |lllj
                                             |||||

    """)


def vampire_art():
    print(r"""
                 /######\
               /##########\
              /   \###/    \
             /     \#/      \
          /\|               |/\
          | | \ ==\    /== / | |
           \|  \<|>\  /<|>/  |/     /|
    \__     |    -   \  -    |     /#|
     \#\     |        |      |   /###|
      \##\   |       \|     |  /#####|
       \###\  |   _______  | /######|
        \####\ | / \/ \/ \|/#######|
        |######\|        |#########|
        |########\______/##########|
        |#########\    /##########/
        |##########\  |#########/\
        /###########\/########/###\
    /################\######/########\
   /##################\###/###########\
  /###################\#/##############\
 /####################/#################\
/###################/####################\
    """)


def ghost_art():
    print(r"""
███████████████████████████████████
███████████████████████████████████
███████████████████████████████████
█████████████▒▒▒▒▒▒▒▒▒█████████████
█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████
███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████
██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████
█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████
█████▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒█████
████▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒████
███▒▒▒▒██████▒▒▒▒▒▒▒▒▒██████▒▒▒▒███
███▒▒▒███▐▀███▒▒▒▒▒▒▒███▀▌███▒▒▒███
███▒▒▒██▄▐▌▄███▒▒▒▒▒███▄▐▌▄██▒▒▒███
███▒▒▒▒██▌███▒▒▒█▒█▒▒▒███▐██▒▒▒▒███
██▒▒▒▒▒▒███▒▒▒▒██▒██▒▒▒▒███▒▒▒▒▒▒██
█▒▒▒▒▒▒▒▒█▒▒▒▒██▒▒▒██▒▒▒▒█▒▒▒▒▒▒▒▒█
█▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒█
█▒▒▒▒█▒▒█▒▒▒▒██▒▒▒▒▒██▒▒▒▒█▒▒█▒▒▒▒█
██▒▒▒█▒▒█▒▒▒▒█▒██▒██▒█▒▒▒▒█▒▒█▒▒▒██
███▒█▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒█▒███
█████▒▒█▒▒▒▐███████████▌▒▒▒█▒▒█████
███████▒▒▒▐█▀██▀███▀██▀█▌▒▒▒███████
███████▒▒▒▒█▐██▐███▌██▌█▒▒▒▒███████
███████▒▒▒▒▒▐▒▒▐▒▒▒▌▒▒▌▒▒▒▒▒███████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████
█████████▒▒█▒█▒▒▒█▒▒▒█▒█▒▒█████████
█████████▒██▒█▒▒▒█▒▒▒█▒██▒█████████
██████████████▒▒███▒▒██████████████
██████████████▒█████▒██████████████
███████████████████████████████████
███████████████████████████████████
    """)


def dragon_art():
    print(r"""
                       _/          ,          .                                          
       , -' )         ( \-------.,')            (\_________________________  
     , ,-/ |          /\_) )     \/            ,' _.----------------------,\ 
   ,',  /, |         /      >--. ,)           / /\\                          
  / ,  //|,'        /'     '\--'\\)          /,'  \\     `         `   ,     
 / ,  // ||       ,'     (.--^( `')         //     \\                \       
( ,  //  ||,___,-'    (___\\  '^^^'        //       \\              ,        
 \  //   ||--.__     (     \`^--)  _____.-'/         \\   `                  
  >'/    ||,        (       \|_(\-'      ,'           \\         \,          
 /,'     ||          \           \      /              \\                    
(/       ||           \           )  ,'(     `     `    \\      ,            
 `       ||\           \      ) ,'  /_  )                \\    \             
         || `.          `.    ,'   /( `.\  \ , \ \,       \\   ,             
   `     || (_`.          ` .'   .'  )  `)'            ,   \\                
         ||  (_ `-v-------  ^--v' , )                      '\\,              
         ||    (    , _,-  /  -./ )'                         `)              
     `   '|     ),  ,'    '     )'                                           
        ' ;    /  ,'          ,'                                             
       /,'    /  /      '    /     , - --- .                                 
       \|    /  (          ,'   '           `.                               
       ('  ,'    `.    "  / ,'                \                              
         ,'        \    ,/,'        '`)   (_   )                             
        /           \ , /'          ,      /  /                              
       .             )  ,       ,         '  /                               
                      )      ,              /                                
       .            ' `|   ,'              /                                 
                    '  |  /              ,'                                  
        |\             | <    ______,---'                                    
        ` \            ','   (                                               
         \ '          /(____ ,`-._,-.                                        
          `.         /      `._, )---)                                       
            `-------'\         `/ \                                          
               )   )  \          ` \                                         
              /  '(    `.         `                                          
         ___,' _, /      `.         .                                        
        ('.---/ \(          .      '|                                        
        /'    `|^'           .     ,                                         
                             .     /                                         
                                  '                                          
                            '    '                                           
                          ,'  ,                                              
                         (_ '                                                                               


    """)


def minotaur_art():
    print(r"""
                                            ,--,  ,.-.
               ,                   \,       '-,-`,'-.' | ._
              /|           \    ,   |\         }  )/  / `-,',
              [ ,          |\  /|   | |        /  \|  |/`  ,`
              | |       ,.`  `,` `, | |  _,...(   (      .',
              \  \  __ ,-` `  ,  , `/ |,'      Y     (   /_L\
               \  \_\,``,   ` , ,  /  |         )         _,/
                \  '  `  ,_ _`_,-,<._.<        /         /
                 ', `>.,`  `  `   ,., |_      |         /
                   \/`  `,   `   ,`  | /__,.-`    _,   `\
               -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                \_,,.) /\    ` /  / ) (-,, ``    ,        |
               ,` )  | \_\       '-`  |  `(               \
              /  /```(   , --, ,' \   |`<`    ,            |
             /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
       ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
      (-, \           ) \ ('_.-._)/ /,`    /
      | /  `          `/ \\ V   V, /`     /
   ,--\(        ,     <_/`\\     ||      /
  (   ,``-     \/|         \-A.A-`|     /
 ,>,_ )_,..(    )\          -,,_-`  _--`
(_ \|`   _,/_  /  \_            ,--`
 \( `   <.,../`     `-.._   _,-`
    """)


def artwork():
    slowprint("Dragon was created by James Goodwin\n"
              "Goblin was created by https://ascii.co.uk/art/goblin\n"
              "Troll created by Veronica Karlsson\n"
              "Skeleton created by Nabis\n"
              "vampire created by VICKY WILKS\n"
              "ghost created by https://textart.sh/topic/ghost\n"
              "Minotaur created by Shanaka Dias\n"
              "door created by https://ascii.co.uk/art/doors\n"
              "Barbarian was inspired by Berserk by Kentaro Miura\n"
              "Mage created by https://www.asciiart.eu/people/occupations/wizards\n"
              "grim-reaper for death was by https://ascii.co.uk/art/death\n"
              "Hunter was created by https://www.asciiart.eu/weapons/bows-and-arrows\n"
              "Ascii text was created using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type"
              "%20Something%20\n"
              "")


loading_screen()
sleep(0.5)
os.system('cls')
intro_to_game()
player = name_of_adventurer()
os.system('cls')
slowprint(f"Oh-hh a worthy name, {player} \nworthy of the champion")
intro_to_game_part_two(player)
goblin_health = goblin_stats()["goblin_health"]
goblin_name = goblin_stats()["name"]
goblin_dmg = goblin_stats()["goblin_dmg"]
skeleton_health = skeleton_stats()["skeleton_health"]
skeleton_name = skeleton_stats()["name"]
skeleton_dmg = skeleton_stats()
skeleton_dmg = skeleton_dmg["skeleton_dmg"]
vampire_health = vampire_stats()["vampire_health"]
vampire_dmg = vampire_stats()["vampire_dmg"]
troll_health = troll_stats()["troll_health"]
troll_dmg = troll_stats()["troll_dmg"]
ghost_health = ghost_stats()["ghost_health"]
ghost_dmg = ghost_stats()["ghost_dmg"]
minotaur_health = minotaur_stats()["minotaur_health"]
minotaur_dmg = minotaur_stats()["minotaur_dmg"]
dragon_health = dragon_stats()["dragon_health"]
dragon_dmg = dragon_stats()["dragon_dmg"]
troll_name = troll_stats()["name"]
minotaur_name = minotaur_stats()["name"]
dragon_name = dragon_stats()["name"]
vampire_name = vampire_stats()["name"]
ghost_name = ghost_stats()["name"]
print("\n Barbarian \n Mage \n Hunter")
while True:
    hero = input("Please chose your hero\n")
    hero = hero.lower()
    if hero == "barbarian":
        os.system('cls')
        barbarian_art()
        barbarian_story()
        os.system('cls')
        hero_stats = barb_stats()
        hero_attacks = barb_attacks()
        hero_items = barb_items()
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
        mage_art()
        mage_story()
        os.system('cls')
        hero_stats = mage_stats()
        hero_attacks = mage_attacks()
        hero_items = mage_items()
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
        hunter_art()
        hunter_story()
        os.system('cls')
        hero_stats = hunt_stats()
        hero_attacks = hunt_attacks()
        hero_items = hunt_items()
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


def fight(hero_stats, hero_items, hero_attacks, monster_dmg, monster_health, monster_name):
    monster_health = monster_health
    monster_dmg = monster_dmg
    counter = hero_items["health_potion"]["uses"]
    combat_health = hero_stats["health"]
    while not combat_health <= 0:
        print(hero_attacks)
        print(hero_items)
        choice = input("please chose a skill form the list above\n")
        choice = choice.lower()
        if choice in hero_items.keys():
            print(f"you used {choice}")
            counter = counter - 1
            temp_health = combat_health + hero_items[choice]["potion_heal"]
            print(counter)
            if counter <= 0:
                print("your health potion is empty")
            if counter > 0:
                if temp_health > hero_stats["health"]:
                    combat_health = hero_stats["health"]
                    print(combat_health)
                else:
                    combat_health = temp_health
                    print(combat_health)
        if choice in hero_attacks.keys():
            monster_health = monster_health - hero_attacks[choice]
            print(f"the {monster_name} has {monster_health} health remaining")
            print(f"you have {combat_health} health remaining")
        if choice not in hero_attacks.keys() and hero_items.keys():
            print("you did not use a valid skill")
            choice = input("please chose a skill from the list above \n")
        else:
            combat_health = combat_health - monster_dmg
            print(f"you have took {monster_dmg} dmg")
            print(combat_health)

        if combat_health <= 0:
            death()
            exit()

        if monster_health <= 0:
            print("you have won")
            break


counter = hero_items["health_potion"]["uses"]
os.system('cls')


def fight(hero_stats, hero_items, hero_attacks, monster_dmg, monster_health, monster_name):
    monster_health = monster_health
    monster_dmg = monster_dmg
    counter = hero_items["health_potion"]["uses"]
    combat_health = hero_stats["health"]
    while not combat_health <= 0:
        print(hero_attacks)
        print(hero_items)
        choice = input("please chose a skill form the list above\n")
        choice = choice.lower()
        if choice in hero_items.keys():
            print(f"you used {choice}")
            counter = counter - 1
            temp_health = combat_health + hero_items[choice]["potion_heal"]
            print(counter)
            if counter <= 0:
                print("your health potion is empty")
            if counter > 0:
                if temp_health > hero_stats["health"]:
                    combat_health = hero_stats["health"]
                    print(combat_health)
                else:
                    combat_health = temp_health
                    print(combat_health)
        if choice in hero_attacks.keys():
            monster_health = monster_health - hero_attacks[choice]
            print(f"the {monster_name} has {monster_health} health remaining")
            print(f"you have {combat_health} health remaining")
        if choice not in hero_attacks.keys() and hero_items.keys():
            print("you did not use a valid skill")
            choice = input("please chose a skill from the list above \n")
        else:
            combat_health = combat_health - monster_dmg
            print(f"you have took {monster_dmg} dmg")
            print(combat_health)

        if combat_health <= 0:
            death()
            exit()

        if monster_health <= 0:
            print("you have won")
            break


two_door_art()
door_choice = two_doors()
door_choice.lower()
if door_choice == "right":
    os.system('cls')
    goblin_description()
    goblin_art()
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=goblin_dmg, monster_health=goblin_health, monster_name=goblin_name)
    sleep(1)
    os.system('cls')

if door_choice == "left":
    os.system('cls')
    skeleton_art()
    skeleton_description()
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=skeleton_dmg, monster_health=skeleton_health, monster_name=skeleton_name)
    sleep(1)
    os.system('cls')

two_door_art()
door_choice_two = two_doors()
door_choice_two.lower()
if door_choice_two == "left":
    os.system('cls')
    troll_art()
    troll_description()
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=troll_dmg, monster_health=troll_health, monster_name=troll_name)
    sleep(1)
    os.system('cls')

if door_choice_two == "right":
    os.system('cls')
    ghost_art()
    ghost_description()
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=ghost_dmg, monster_health=ghost_health, monster_name=ghost_name)
    sleep(1)
    os.system('cls')

three_door_art()
door_choice_three = three_door()
door_choice_three.lower()
if door_choice_three == "right":
    os.system('cls')
    # add description of fight
    minotaur_art()
    minotaur_description()
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=minotaur_dmg, monster_health=troll_health, monster_name=troll_name)
    sleep(1)
    os.system('cls')
if door_choice_three == "center":
    os.system('cls')
    vampire_art()
    vampire_description()
    # add description of fight
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=vampire_dmg, monster_health=vampire_health, monster_name=vampire_name)
    sleep(1)
    os.system('cls')

if door_choice_three == "left":
    os.system('cls')
    minotaur_art()
    minotaur_description()
    # add description of fight
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=minotaur_dmg, monster_health=minotaur_health, monster_name=minotaur_name)
    sleep(1)
    os.system('cls')

boss_door_art()
boss_door = boss_door()
boss_door.lower()
if boss_door == "open":
    os.system('cls')
    dragon_art()
    dragon_description()
    fight(hero_stats=hero_stats, hero_items=hero_items, hero_attacks=hero_attacks,
          monster_dmg=dragon_dmg, monster_health=dragon_health, monster_name=dragon_name)
ending_scene()
ending_text(player)
artwork()
exit()
