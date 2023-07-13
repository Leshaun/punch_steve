class Move:
    def __init__(self, name, min_dmg, max_dmg, type):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.type = type

class Opponent:
    def __init__(self, name, hitpoints, weakness):
        self.name = name
        self.hitpoints = hitpoints
        self.weakness = weakness
