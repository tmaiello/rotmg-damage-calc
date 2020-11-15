__author__ = "Tyler Maiello"

# Item class to create item objects with stats
# Some items come with stat additions or subtractions, this is to manage that
class Item:
    # unfortunately, "def" is a keyword :)
    # slots are objects of items which contain active stats
    def __init__(self, life, mana, att, defense, spd, dex, vit, wis):
        self._life = life
        self._mana = mana
        self._att = att
        self._defense = defense
        self._spd = spd
        self._dex = dex
        self._vit = vit
        self._wis = wis
    
    @property
    def life(self):
        return self._life
    
    @property
    def mana(self):
        return self._mana

    @property
    def att(self):
        return self._att
    
    @property
    def defense(self):
        return self._defense

    @property
    def spd(self):
        return self._spd

    @property
    def dex(self):
        return self._dex

    @property
    def vit(self):
        return self._vit

    @property
    def wis(self):
        return self._wis
    
    @life.setter
    def life(self, life):
        self._life = life

    @mana.setter
    def mana(self, mana):
        self._mana = mana

    @att.setter
    def att(self, att):
        self._att = att
        
    @defense.setter
    def defense(self, defense):
        self._defense = defense

    @spd.setter
    def spd(self, spd):
        self._spd = spd

    @dex.setter
    def dex(self, dex):
        self._dex = dex

    @vit.setter
    def vit(self, vit):
        self._vit = vit

    @wis.setter
    def wis(self, wis):
        self._wis = wis