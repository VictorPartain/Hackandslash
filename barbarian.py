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
        "enrage": {
            "hero_attacks": 40,
            "enrage": 3
        }

    }


def hero_items():
    return {
        "health_potion": {
            "potion_heal": 30,
            "uses": 3,
        }
    }
