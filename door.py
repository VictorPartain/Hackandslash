from time import sleep


def slowprint(msg):
    for c in msg:
        print(c, end="", flush=True)
        sleep(0.01)
    print()


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