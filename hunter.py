hunter_dmg = 200
hunter_health = 200

def hero_stats():
    return{
        "dmg": 200,
        "health": 200
    }
def hero_attacks():
    return{
        "quickshot": 200
    }

def hero_buffs():
   return{
        "heal": hero_stats()["health"] * 0.30
   }


def hero_items():
    return {
        "health_potion": {
            "potion_heal": 30,
            "uses": 3,
        }
    }

