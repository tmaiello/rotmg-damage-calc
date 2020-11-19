__author__ = "Tyler Maiello"
from statistics import mean

def damage_solve(character):
    return {"dps":((mean({character.slot_1['_min_damage'], character.slot_1['_max_damage']-1}) * (0.5 + character.att/50)) * character.slot_1['_num_projectiles']) * (1.5 + 6.5*(character.dex/75))}
    # return {"dps":((0.5 + character.att/50)*(mean({220,275})))}
    # return {"dps":((mean({220, 274}) * (0.5 + character.att/50)) * 1) * (1.5 + 6.5*(character.dex/75))}
