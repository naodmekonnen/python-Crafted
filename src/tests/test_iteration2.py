from evercraft.character import *

def test_class_fighter():
    assert Fighter

def test_new_class_name():
    fighter1 = Fighter('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 12)
    assert fighter1.name == 'roger'

def test_hitpoints1():
    fighter1 = Fighter('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 12)
    assert fighter1.hitpoints == 11

def test_hitpoints10():
    fighter1 = Fighter('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 12)
    fighter1.level_up()
    assert fighter1.hitpoints == 21

def test_level_up():
    fighter1 = Fighter('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 12)
    fighter1.level_up()
    assert fighter1.dice_roll == 15

def test_AC_fighter():
     fighter1 = Fighter('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 12)
     assert fighter1.arclass == 14

def test_class_rogue():
    assert Rogue

def test_new_crit_modifier():
    fighter1 = Fighter('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 20)
    fighter2 = Fighter('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 20)
    fighter1.make_attack(fighter2)
    assert fighter2.hitpoints == 5

def test_rogue_attack():
    rogue1 = Rogue('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 20)
    rogue2 = Rogue('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 20)
    rogue1.make_attack(rogue2)
    assert rogue2.hitpoints == -3

def test_rogue_dex():
    rogue1 = Rogue('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 15)
    assert rogue1.attack == 2

def test_rogue_alignment():
    rogue1 = Rogue('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 15)
    assert rogue1.alignment == 'evil' or rogue1.alignment == 'neutral'

def test_monk_class():
    assert Monk

def test_hitpoints10():
    monk1 = Monk('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 12)
    monk1.level_up()
    assert monk1.hitpoints == 12

def test_monk_attack():
    monk1 = Monk('roger', 'good', 10, 1000, 15, 12, 12, 10, 10, 10, 12)
    assert monk1.attack == 5

def test_monk_AC_positive():
    monk1 = Monk('roger', 'good', 10, 1000, 15, 12, 12, 12, 10, 10, 12)
    assert monk1.arclass == 12

def test_monk_AC_negatory():
    monk1 = Monk('roger', 'good', 10, 1000, 15, 12, 12, 8, 10, 10, 12)
    assert monk1.arclass == 11

def test_Paladin():
    assert Paladin

def test_hitpoints1():
    paladin1 = Paladin('roger', 'good', 10, 1000, 15, 12, 12, 8, 10, 10, 12)
    assert paladin1.hitpoints == 9
     
def test_hitpoints_level():
    paladin1 = Paladin('roger', 'good', 10, 1000, 15, 12, 12, 8, 10, 10, 12)
    paladin1.level_up()
    assert paladin1.hitpoints == 17

def test_dice_roll_modifier():
    paladin1 = Paladin('roger', 'good', 10, 1000, 10, 12, 12, 10, 10, 10, 17)
    fighter1 = Fighter('roger', 'evil', 10, 1000, 10, 12, 12, 10, 10, 10, 17)
    paladin1.make_attack(fighter1)
    assert fighter1.hitpoints == 8

def test_paladin_crit():
    paladin1 = Paladin('roger', 'good', 10, 1000, 10, 12, 12, 10, 10, 10, 18)
    fighter1 = Fighter('roger', 'evil', 10, 1000, 10, 12, 12, 10, 10, 10, 17)
    paladin1.make_attack(fighter1)
    assert fighter1.hitpoints == 6


     







   









# Fighter('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 12)
     
