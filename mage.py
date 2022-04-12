def hero_stats():
    return{
        "health": 100,
        "dmg": 300
    }


def hero_attacks():
    return{
        "fireball": 300
    }


def hero_buffs():
    return{
        "heal": hero_stats()["health"] * 0.30
    }
