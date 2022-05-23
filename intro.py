from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.02)
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
              f"\nLets see what you can do {player}")


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
