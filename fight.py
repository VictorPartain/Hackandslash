import ending


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
            ending.death()
            exit()

        if monster_health <= 0:
            print("you have won")
            break
