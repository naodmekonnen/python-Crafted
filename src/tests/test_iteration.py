from evercraft import *

def test_class_character():
    assert Character

def test_name_attribute():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.name is not None 

def test_name_value():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.name == 'Roger'

def test_alignment_att():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.alignment == 'evil'

def test_AC_att():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.ac is not None

def test_AC_att():
    character1 = Character('Roger', 'evil', 10, 12,'hi')
    assert character1.ac == 10

def test_hitpoints():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.hitpoints is not None

def test_hitpoint_value():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.hitpoints == 12

def test_expoints_value():
    character1 = Character('Roger', 'evil', 10, 12, 'hi')
    assert character1.expoints is not None

def test_expoints_clown():
    character1 = Character('Roger', 'evil', 10, 12, 0)
    assert character1.expoints == 0

def test_ability_scores():
    character1 = Character('Roger', 'evil', 10, 12, 0)
    assert character1.strength is not None
    assert character1.dexterity is not None
    assert character1.constitution is not None
    assert character1.wisdom is not None
    assert character1.intelligence is not None
    assert character1.charisma is not None

def test_passed_scores():
    character1 = Character('roger', 'good', 10, 12, 0, 10, 10, 10, 10, 10, 10)
    assert character1.strength == 10
    assert character1.dexterity == 10
    assert character1.constitution == 10
    assert character1.wisdom == 10
    assert character1.intelligence == 10
    assert character1.charisma == 10

def test_attack():
    character1 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character2 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character1.can_attack(15, character2)
    assert character2.hitpoints == 4

def test_attack_2():
    character1 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character2 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character1.can_attack(20, character2)
    assert character2.hitpoints == 3

def test_can_take_damage():
    character1 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character2 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character1.take_damage(15, character2)
    assert character1.hitpoints == 4

def test_can_take_damage1():
    character1 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    assert character1.is_alive == True

def test_can_take_damage2():
    character1 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character2 = Character('roger', 'good', 10, 0, 10, 10, 10, 10, 10, 10)
    character1.take_damage(15, character2)
    character1.take_damage(15, character2)
    character1.take_damage(15, character2)
    character1.take_damage(15, character2)
    character1.take_damage(15, character2)
    assert character1.is_alive == False