def two_doors():
    door = input("Choose a door \n left or right \n")
    while True:
        if door == "left":
            return door

        if door == "right":
            return door
        else:
            print("you have not chosen a valid door, please pick a valid door")
            door = input("Choose a door \n left or right \n")


def three_door():
    door = input("Choose a door \n left, right or center \n")
    while True:
        if door == "left":
            return door

        if door == "right":
            return door

        if door == "center":
            return door
        else:
            print("you have not chosen a valid door, please pick a valid door")
            door = input("Choose a door \n left, right or center \n")


def boss_door():
    door = input("there is only one door remaining, \n please type continue to continue to the boss \n")
    while True:
        if door == "continue":
            return door
        else:
            print("you did not choose a valid door, please try again")
            door = input("there is only one door remaining, \n please type continue to continue to the boss \n")