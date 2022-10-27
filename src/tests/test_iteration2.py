from evercraft import *

def test_class_fighter():
    assert Fighter

def test_new_class_name():
    fighter1 = Fighter('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 12)
    assert fighter1.name == 'roger'

def test_hitpoints1():
    fighter1 = Fighter('roger', 'good', 10, 0, 15, 12, 12, 10, 10, 10, 12)
    assert fighter1.hitpoints == 10



   
     
