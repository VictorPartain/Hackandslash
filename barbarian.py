def hero_stats():
    return {
        "dmg": 100,
        "health": 1000,
        "defense": 30,
    }


def hero_attacks():
    return {
        "slash": 40
    }


def hero_buffs():
    return {
        "enrage": 3,
        "heal": hero_stats()["health"] * 0.30

    }
