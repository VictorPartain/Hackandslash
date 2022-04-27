def loading_screen():
    print(r"""
    
  ___ ___                   __                         .___         .__                   .__     
 /   |   \ _____     ____  |  | __ _____     ____    __| _/   ______|  |  _____     ______|  |__  
/    ~    \\__  \  _/ ___\ |  |/ / \__  \   /    \  / __ |   /  ___/|  |  \__  \   /  ___/|  |  \ 
\    Y    / / __ \_\  \___ |    <   / __ \_|   |  \/ /_/ |   \___ \ |  |__ / __ \_ \___ \ |   Y  \
 \___|_  / (____  / \___  >|__|_ \ (____  /|___|  /\____ |  /____  >|____/(____  //____  >|___|  /
       \/       \/      \/      \/      \/      \/      \/       \/            \/      \/      \/ 
    """)


def intro_to_game():
    print("Hello Adventurer, \nI welcome you to a story \na story of The Champion")
    print("But before we begin I must ask you a few questions \nmy first request is that tell me your name adventurer")


def name_of_adventurer():
    player = input("Please type your name \n")
    return player


def intro_to_game_part_two(player):
    print(f"I am glad that you joined us {player}")
    print("Now that I know your name we must begin your adventure, \nThere is only one more "
          "step needed to continue and that is to chose your hero")
    print("To chose your hero please type one of the three options")
