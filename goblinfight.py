def goblin_encounter():
    print("A goblin has appeared please use on of your skills")
    print("Here are your skills")

    while not health <= 0:
        print(hero_attacks)
        attack = input(" ")
        if attack == "slash":
            goblin_health = goblin_health - slash
            health = health - goblin_dmg
            print(f"the goblin has {goblin_health} health remaining")
            print(f"you have {health} health remaining")

        # if attack == "2":
        #  print(f"your currant damage using slash is {slash}")
        #    print("The goblin has attacked you")
        #    barb_health = barb_health - goblin_dmg
        #    print(f"You have {barb_health} health remaining ")

        if health <= 0:
            print("you have died")
            exit()

            if goblin_health <= 0:
                print("you have won")
                break
        from barbarian import hero_stats
        from barbarian import hero_attacks
        from barbarian import hero_buffs
        hero_stats = hero_stats()
        hero_attacks = hero_attacks()
        hero_buffs = hero_buffs()
        health = hero_stats["barb_health"]
        slash = hero_attacks["slash"]
        enrage = hero_buffs["enrage"]
        goblin_health = 70
        goblin_dmg = 30
        slash = hero_attacks()["slash"]