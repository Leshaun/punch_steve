from list import moves
from random import randint
from list import steve

def punch():
    damage = randint(moves[0].min_dmg, moves[0].max_dmg)
    if steve.weakness == moves[0].type:
        damage = damage * 2
        return damage
    else:
        return damage

