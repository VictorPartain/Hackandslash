from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.06)
    print()


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
