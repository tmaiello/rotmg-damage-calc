__author__ = "Tyler Maiello"
from functions import character

def return_maxed_stats(class_name):
    if class_name.lower() == "archer":
        return character.Character(700,252,75,25,50,50,40,50, None, None, None, None)
    elif class_name.lower() == "assassin":
        return character.Character(720,252,60,25,75,75,40,60, None, None, None, None)
    elif class_name.lower() == "huntress":
        return character.Character(700,252,75,25,50,50,40,50, None, None, None, None)
    elif class_name.lower() == "knight":
        return character.Character(770,252,50,40,50,50,75,50, None, None, None, None)
    elif class_name.lower() == "mystic":
        return character.Character(670,385,60,25,60,50,40,75, None, None, None, None)
    elif class_name.lower() == "necromancer":
        return character.Character(770,252,60,25,50,60,30,75, None, None, None, None)
    elif class_name.lower() == "ninja":
        return character.Character(770,252,70,25,60,70,40,70, None, None, None, None)
    elif class_name.lower() == "paladin":
        return character.Character(770,252,50,25,50,50,40,75, None, None, None, None)
    elif class_name.lower() == "priest":
        return character.Character(770,252,50,25,50,50,40,75, None, None, None, None)
    elif class_name.lower() == "rogue":
        return character.Character(770,252,50,25,75,75,40,50, None, None, None, None)
    elif class_name.lower() == "sorcerer":
        return character.Character(770,252,60,25,60,60,75,60, None, None, None, None)
    elif class_name.lower() == "trickster":
        return character.Character(770,252,65,25,75,75,40,60, None, None, None, None)
    elif class_name.lower() == "warrior":
        return character.Character(770,252,75,25,50,50,75,50, None, None, None, None)
    elif class_name.lower() == "wizard":
        return character.Character(770,252,75,25,50,75,40,60, None, None, None, None)
    else:
        raise ValueError("Invalid Class",class_name)