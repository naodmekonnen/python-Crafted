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

def test_modifier():
    character1 = Character('roger', 'good', 10, 0, 12, 10, 10, 10, 10, 10, 12)
    character1.modifier()
    assert character1.attack == 2

def test_modifier_dice():
    character1 = Character('roger', 'good', 10, 0, 12, 10, 10, 10, 10, 10, 12)
    character1.modifier()
    assert character1.dice_roll == 13
    
def test_modifier2():
    character1 = Character('roger', 'good', 10, 0, 15, 10, 10, 10, 10, 10, 12)
    character1.modifier()
    assert character1.dice_roll == 14
    assert character1.attack == 3

def test_modifier3():
    character1 = Character('roger', 'good', 10, 0, 20, 10, 10, 10, 10, 10, 10)
    character1.modifier()
    assert character1.attack == 6
    assert character1.dice_roll == 15

def test_modifier4():
    character1 = Character('roger', 'good', 10, 0, 2, 10, 10, 10, 10, 10, 10)
    character1.modifier()
    assert character1.attack == 1
    assert character1.dice_roll == 6

def test_dex():
    character1 = Character('roger', 'good', 10, 0, 10, 1, 10, 10, 10, 10, 10)
    character1.modifier()
    assert character1.arclass == 5

def test_dex_complete():
    character1 = Character('roger', 'good', 10, 0, 10, 12, 10, 10, 10, 10, 10)
    character1.modifier()
    assert character1.arclass == 11

def test_constitution():
    character1 = Character('roger', 'good', 10, 0, 10, 12, 12, 10, 10, 10, 10)
    character1.modifier()
    assert character1.hitpoints == 6

def test_expoints():
    character1 = Character('roger', 'good', 10, 0, 10, 12, 12, 10, 10, 10, 10)
    character2 = Character('roger', 'good', 10, 0, 10, 12, 12, 10, 10, 10, 10)
    character1.modifier()
    character1.can_attack(character2)
    assert character2.hitpoints == 4
    assert character1.expoints == 10
    
def test_check_level():
    character1 = Character('roger', 'good', 10, 0, 10, 12, 12, 10, 10, 10, 10)
    character2 = Character('roger', 'good', 10, 0, 10, 12, 12, 10, 10, 10, 10)
    assert character1.level == 1
   
def test_check_level_up():
    character1 = character1 = Character('roger', 'good', 10, 1000, 10, 12, 12, 10, 10, 10, 10)
    character1.modifier()
    character1.check_level()
    assert character1.level == 2
    assert character1.hitpoints == 11

def test_new_modifier():
    character1 = Character('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 10)
    assert character1.dice_roll == 12

def test_new_modifier2():
    character1 = Character('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 10)
    




