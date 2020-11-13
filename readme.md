# RotMG Damage Calculator


#### Author: Tyler Maiello

## About

This App is my take on a damage calculator for RotMG since the popular one a lot of people used is on flash <3

## Notes


### RANGE CALC (Info From Wiki)

Projectile Speed (in t/s) * Projectile Lifetime (in seconds) = Range (in tiles)


### DAMAGE CALC (Info From Wiki)
HP (Hit Points)
Your health. When it reaches 0 (Or in rare cases, -1), you die.
When you have only 20% of your health and less, your character starts to blink red and you should drink some health potions or nexus before you take any further damage.

MP (Magic/Mana Points)
Your magic. This is expended to use abilities. Usage depends on what class and ability item tier you are using.

ATT (Attack)
Increases the amount of damage done by weapons. Attack does not affect ability damage.
Damage Multiplier if Weak = 0.5
Damage Multiplier normal = 0.5 + ATT / 50 = (ATT + 25) / 50
Damage Multiplier with Damaging = Normal * 1.25
Therefore,
Damage = Random(MinDamage, MaxDamage) * Damage Multiplier
Starting with a base of 50% of weapon damage at 0 ATT, each point increases damage by 2% of weapon damage. Examples:
10 ATT Priest with a Fire Wand (30-55 DMG) = 21-38 DMG
83 ATT Warrior with a Sword of Acclaim (220-275 DMG) = 475-594 DMG
Note: In game, the highest weapon base damage value is actually never rolled. Thus the effective weapon base damage range always is one less than stated in the weapon description. For example, the effective weapon base damage range of the Fire Wand (originally 30-55 DMG) is 30-54 DMG. Taking this into account, the previous two examples would change as follows:
10 ATT Priest with a Fire Wand (30-54 DMG) = 21-37 DMG
83 ATT Warrior with a Sword of Acclaim (220-274 DMG) = 475-591 DMG

DEF (Defense)
Decreases the amount of damage taken.
Straight 1 point per 1 damage reduction, but caps at 90% of total damage. This means that every shot will do at least 10% of its damage to the player. Example:
60 DMG Attack against 20 DEF = 40 DMG
60 DMG Attack against 54 or higher DEF = 6 DMG

SPD (Speed)
Increases the speed at which the character moves. Base (0) is 4 tiles per second, then each point adds about 0.07467 tiles per second.
Actual speed in T/s (tiles per second) = 4 + 5.6 * (SPD / 75) = 5.6 * (SPD + 53.5) / 75
50 SPD: 7.733 T/s
75 SPD: 9.6 T/s
T/s while Speedy: Normal * 1.5 (75 SPD with Speedy means 14.4 T/s movement speed)

DEX (Dexterity)
Increases the speed at which the character attacks. Base (0) is 1.5 attacks per second, then each point adds about 0.0867 attacks per second.
A/s (attacks per second) = 1.5 + 6.5 * (DEX / 75) = 6.5 * (DEX + 17.3) / 75
50 DEX: 5.833 A/s (350 per minute)
75 DEX: 8 A/s (480 per minute)
A/s while Berserk: Normal * 1.25 

VIT (Vitality)
Increases the speed at which hit points are recovered. Base (0) is 1.0 HP per second, then each point adds about 0.24 HP per second.
HP/s (hp per second) = 1 + 0.24 * VIT = 0.24 * (VIT + 8.3)
40 VIT: 10.6 HP/s
75 VIT: 19 HP/s
HP/s while Healing: Normal + 20 (75 VIT with Healing means 39 HP/s)

WIS (Wisdom)
Increases the speed at which magic points are recovered. Base (0) is 0.5 MP per second, then each point adds about 0.12 MP per second.
MP/s (mp per second) = 0.5 + 0.12 * WIS = 0.12 * (WIS + 8.3)
50 WIS: 6.5 MP/s
75 WIS: 9.5 MP/s
Also modifies the intensity, range, and duration of Priest Tomes, Paladin Seals, and Mystic Orbs, the radius and damage of Necromancer Skulls, and the number of targets and damage of Sorcerer Scepters, but only when the user’s WIS stat is more than 50.
modified value = initial value * (1 + (WIS - 50) / 50)
Your ability potential multiplier can’t go below 1 (formula above only applies when Wisdom is 50 or higher). At 75 Wisdom your ability potential is 1.5 times that of if you had 50 Wisdom.


### ID TYPES
ID: Usable Characters: Type:

1 Warrior, Knight, Paladin - Weapon (Sword)

2 Rogue, Assassin, Trickster - Weapon (Dagger)

3 Archer, Huntress - Weapon (Bow)

4 Priest - Armor (Cloth)

5 Knight - Special (Helm)

6 Archer, Huntress, Rogue, Assassin, Trickster - Armor (Leather)

7 Warrior, Knight, Paladin - Armor (Heavy)

8 Priest, Sorcerer - Weapon (Wand)

9 All Chars - Ring

10 Nothing?

11 Wizard - Special (Spell)

12 Paladin - Special (Seal)

13 Rogue - Special (Cloak)

14 Wizard, Priest, Necromancer, Mystic, Sorcerer - Armor (Robe)

15 Archer - Special (Quiver)

16 Warrior - Special (Helm?)

17 Wizard, Necromancer, Mystic - Weapon (Staff)

18 Assassin - Special (Poison)

19 Necromancer - Special (Skull)

20 Huntress - Special (Trap)

21 Mystic - Special (Orb)

22 Trickster - Special (Prism)

23 Sorcerer - Special (Scepter)
