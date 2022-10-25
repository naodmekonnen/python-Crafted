from evercraft import *

def test_class_character():
    assert Character

def test_name_attribute():
    character1 = Character()
    assert character1.name is not None 

def test_name_value():
    character1 = Character('Roger')
    assert character1.name == 'Roger'

def test_alignment_att():
    character1 = Character('Roger', 'evil')
    assert character1.alignment == 'evil'

def test_AC_att():
    character1 = Character('Roger', 'evil', 'anything')
    assert character1.ac is not None

def test_AC_att():
    character1 = Character('Roger', 'evil', 10)
    assert character1.ac == 10

def test_hitpoints_value():
    character1 = Character('Roger', 'evil', 10, 'yo')
    assert character1.hitpoints

