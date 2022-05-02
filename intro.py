from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.06)
    print()


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
