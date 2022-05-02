from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.06)
    print()


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
