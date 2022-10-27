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





   









# Fighter('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 12)
     
