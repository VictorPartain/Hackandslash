# door = input("what door would you like to chose \n left or right \n")
# while True:
#     if door == "left":
#         break
#     elif door == "right":
#         break
#     else:
#         print("please choose a valid door")
#         door = input("what door would you like to chose \n left or right \n")
#
# if door == "left":
#     print("a skeleton emerges from the shadows")
#     print("it is time to fight again")
#     print(f"the skeleton has {skeleton_health} health  good luck hero")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#         if choice in hero_attacks.keys():
#             skeleton_health = skeleton_health - hero_attacks[choice]
#             combat_health = combat_health - skeleton_dmg
#             print(f"you have {combat_health} health remaining")
#             print(f"the skeleton has {skeleton_health} health remaining")
#         else:
#             print("there is no attacked named that")
#             combat_health = combat_health - skeleton_dmg
#             print(f"you took {skeleton_dmg} damage and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if skeleton_health <= 0:
#             print("you have won")
#             break

# elif door == "right":
#     print("it is time to fight again")
#     print(" a skeleton emerges from the corner of the room")
#     print(f"the skeleton has {skeleton_health} health remaining good luck hero")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input()
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#
#         if choice in hero_buffs.keys():
#             combat_health = combat_health + hero_buffs[choice]
#             combat_health = combat_health - skeleton_dmg
#             print(f"you used {choice}")
#
#         if choice in hero_attacks.keys():
#             skeleton_health = skeleton_health - hero_attacks[choice]
#             combat_health = combat_health - skeleton_dmg
#             print(f"you have {combat_health} health remaining")
#             print(f"the skeleton has {skeleton_health} health remaining")
#         else:
#             print("there is no attacked named that")
#             combat_health = combat_health - skeleton_dmg
#             print(f"you took {skeleton_dmg} damage and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if skeleton_health <= 0:
#             print("you have won")
#             break
# todo: This is broken logic in your if statement.
# door2 = input("what door would you like to chose \n left or right \n")
# while True:
#     if door2 == "left":
#         break
#     elif door2 == "right":
#         break
#     else:
#         print("please choose a valid door")
#         door2 = input("what door would you like to chose \n left or right \n")

# if door2 == "right":
#     print("a poltergeist appears from the floor")
#     print("prepare your self brave hero")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#         if choice in hero_attacks.keys():
#             poltergeist_health = poltergeist_health - hero_attacks[choice]
#             combat_health = combat_health - poltergeist_dmg
#             print(f"you have {combat_health} health remaining")
#             print(f"the troll has {poltergeist_health} remaining")
#         else:
#             print("there is not an attack named that")
#             combat_health = combat_health - poltergeist_dmg
#             print(f"you have taken{poltergeist_dmg} you have {combat_health} remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if troll_health <= 0:
#             print("you have won")
#             break
    # todo: adding spacing and new lines to have it read smoother
    # todo: Does it matter that the player knows about negative number of health or just they won?
# if door2 == "left":
#     print("A troll is waiting for you prepared to attack")
#     print("get ready to fight adventurer")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_attacks.keys():
#             troll_health = troll_health - hero_attacks[choice]
#             combat_health = combat_health - troll_dmg
#             print(f"you have {combat_health} health remaining")
#             if troll_health < 0:
#                 print("you have won")
#             else:
#                 print(f"the troll has {troll_health} remaining")
#         else:
#             print("there is not attacked named that")
#             combat_health = combat_health - troll_dmg
#             print(f"you took {troll_dmg} damage and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if troll_health <= 0:
#             print("you have won")
#             break
#
# door3 = input("what door would you like to chose \n left , right or center \n")
# while True:
#     if door3 == "left":
#         break
#     elif door3 == "right":
#         break
#     elif door3 == "center":
#         break
#     else:
#         print("please choose a valid door")
#         door = input("what door would you like to chose \n left, right or center\n")
# if door3 == "right":
#     print("hero you have chosen the wrong door \n you must now fight the minotaur in his own territory \n I wish you "
#           "the best of luck adventurer,\n also the minotaur has its own unique skill be aware of "
#           "this.")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#         if choice in hero_attacks.keys():
#             minotaur_health = minotaur_health - hero_attacks[choice]
#             combat_health = combat_health - minotaur_dmg
#             print(f"hero you have {combat_health} health remaining")
#             print(f"the minotaur has {minotaur_health} health remaining")
#             print("continue fighting brave adventurer")
#         else:
#             print("there is no attacked named that")
#             combat_health = combat_health - minotaur_dmg
#             print(f"you took {minotaur_dmg} damage and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if minotaur_health <= 0:
#             print("you have triumphed")
#             exit()
# if door3 == "left":
#     print("hero you have chosen the wrong door \n you must now fight the minotaur in his own territory \n I wish you "
#           "the best of luck adventurer,\n also the minotaur has its own unique skill be aware of "
#           "this.")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#         if choice in hero_attacks.keys():
#             minotaur_health = minotaur_health - hero_attacks[choice]
#             combat_health = combat_health - minotaur_dmg
#             print(f"hero you have {combat_health} health remaining")
#             print(f"the minotaur has {minotaur_health} health remaining")
#             print("continue fighting brave adventurer")
#         else:
#             print("there is no attacked named that")
#             combat_health = combat_health - minotaur_dmg
#             print(f"you took {minotaur_dmg} damage and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if minotaur_health <= 0:
#             print("you have triumphed")
#             exit()
#
# # still a work in progress
# if door3 == "center":
#     print("a vampire falls from the ceiling staring at you")
#     print("brace yourself adventurer and get ready for a fight")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#         if choice in hero_attacks.keys():
#             vampire_health = vampire_health - hero_attacks[choice]
#             combat_health = combat_health - vampire_dmg
#             print(f"you have {combat_health} health remaining")
#             print(f"the vampire has {vampire_health} health remaining")
#         else:
#             print("there is no attacked named that")
#             combat_health = combat_health - vampire_dmg
#             print(f"you took {vampire_dmg} damage and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died")
#             exit()
#         if vampire_health <= 0:
#             print("you have won")
#             break
# boss_door = input("there is only one door remaining please type continue \n")
# while True:
#     if door == "continue":
#         break
#     else:
#         print("please choose a valid door")
#         door = input("please type continue \n")
# print("there is only one door remaining please type continue")
# boss_door = input(" ")
# if boss_door == "continue":
#     print("a giant blob is in the center of the room get prepared adventurer")
#     print("the boss has awakened")
#     while not combat_health <= 0:
#         print(hero_attacks)
#         print(hero_buffs)
#         print(hero_items)
#         choice = input(" ")
#         if choice in hero_items.keys():
#             print(f"you used {choice}")
#             counter = counter - 1
#             temp_health = combat_health + hero_items[choice]["potion_heal"]
#             if counter == 0:
#                 print("your health potion is empty")
#                 combat_health = combat_health - goblin_dmg
#                 print(f"you have took{goblin_dmg}")
#
#             if temp_health > combat_health:
#                 combat_health = combat_health
#             else:
#                 combat_health = temp_health
#         if choice in hero_attacks.keys():
#             blob_health = blob_health - hero_attacks[choice]
#             combat_health = combat_health - blob_dmg
#             print(f"you have {combat_health} health remaining hero you got this")
#             print(f"the blob has {blob_health} health remaining")
#         else:
#             print(f"hero there isn't an attacked named that")
#             combat_health = combat_health - blob_dmg
#             print(f"you took {blob_dmg} and have {combat_health} health remaining")
#         if combat_health <= 0:
#             print("you have died hero")
#             exit()
#         if blob_health <= 0:
#             print("you have won")
#             print("Congratulations on your victory")
#             exit()
