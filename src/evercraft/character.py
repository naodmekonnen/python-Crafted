# import random for later use of alignment selection
import random

# begin making the character class (blueprint) that will be the basis for the individual characters generated below
class Character:
    # class level attributes that we use to adjust dice rolls, abilities, attacks, crits, etc
    level_addition = 5
    dice_roll_addition = 1
    attack_modifier = 1
    crit_modifier = 2
    attack_roll_modifier = 0

    # initializer that allows us to pass in necessary values during testing. called every time an object is created from a class
    # note---dice roll is an attack roll passed in (bad naming convention sorry!)
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll):
        
        #values passed in from test, some passed in, some base values
        self.name = name
        self.alignment = alignment
        self.expoints = expoints
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

        #base attack value + the modifier
        self.attack = 1 + self.modifier('strength')

        # defensive programming to reset attack to 1 if it drops below 1
        if self.attack < 1:
            self.attack = 1
        self.is_alive = True
        self.dice_roll = dice_roll + self.modifier('strength')
        self.level = 1
        self.hitpoints = 5 + self.modifier('constitution')
        self.arclass = arclass + self.modifier('dexterity')

# modifier that adjusts abilities passed in (based on game rules)
    def modifier(self, ability):
        return (getattr(self, ability) - 10)//2
# base function that handles basic attacks. pass in another character in instance to set up fight
    def make_attack(self, enemy):
        if self.dice_roll >= 20:
            self.attack *= self.crit_modifier
        if self.dice_roll >= enemy.arclass:
            enemy.hitpoints -= self.attack
            self.expoints += 10
# base function that handles basic damage taken. pass in another character in instance to set up fight
    def take_damage(self, enemy):
        if self.dice_roll == 20:
            self.attack *= crit_modifier
        if self.dice_roll >= self.arclass:
            self.hitpoints -= self.attack
        if self.hitpoints == 0:
            self.is_alive = False

# calculates levels gained based on experience points
    def level_up(self):
        if self.expoints >= 1000:
            self.level += 1
            self.hitpoints += self.level_addition
            self.dice_roll += self.dice_roll_addition

# New child class, inherits attributes and methods from parent(character) class
class Fighter(Character):
#changes how many hitpoints are gains per level
    level_addition = 10
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll):

# super function used to give access to methods and properties of a parent or sibling class.
        super().__init__(name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll)
        
# 10 hitpoints to base
# adds an extra 2 points to armor class plus dexterity        
        self.hitpoints = 10 + self.modifier('constitution')
        self.arclass += 2 + self.modifier('dexterity')

# New child class, inherits attributes and methods from parent(character) class
# crit modifier: multiplies by crits by 3 instead of 2
# random.choice-selects neutral or evil(randomly chooses from list- random must be imported) even if good is passed in)   
class Rogue(Character):
    crit_modifier = 3
    alignment_list = ["neutral", "evil"]
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll):
        super().__init__(name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll)
        self.attack = 1 + self.modifier('dexterity')
        self.alignment = random.choice(self.alignment_list)

# New child class, inherits attributes and methods from parent(character) class

class Monk(Character):
    # 6 points of hp per level instead of 5
    level_addition = 6
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll):
        super().__init__(name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll)
        self.hitpoints = 6 + self.modifier('constitution')
        self.attack = 3 + self.modifier('strength')
        # adds wisdom modifier to armor class as well as dex as long as wisdom is positive
        if self.modifier('wisdom') < 0:
            self.arclass = self.arclass
        else: 
            self.arclass = self.arclass + self.modifier('wisdom')
        
class Paladin(Character):
    level_addition = 8
    # + 2 roll and damage modifier for fighting evil
    attack_roll_modifier = 2
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll):
        super().__init__(name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll)
        # hardsets alignment to good
        self.alignment = 'good'
        self.hitpoints = 8 + self.modifier('constitution')
    # if the enemy is evil, we get a +2 to attack roll, +2 to attack, and triple damage on crit
    # able to use attack roll modifier on both the roll itself and the attack itself as a bonus
    def make_attack(self, enemy):
        if enemy.alignment == 'evil':
            if self.dice_roll + self.attack_roll_modifier >= 20:
                self.attack *= (self.crit_modifier + 1)
            if self.dice_roll + self.attack_roll_modifier >= enemy.arclass:
                enemy.hitpoints -= self.attack + self.attack_roll_modifier
                self.expoints += 10
        else: 
            if self.dice_roll >= 20:
                self.attack *= self.crit_modifier
            if self.dice_roll >= enemy.arclass:
                enemy.hitpoints -= self.attack
                self.expoints += 10
    
    



















#     self.hitpoints = 10 + self.modifier('constitution')

    # if   self.strength == 1:
        #         self.attack -=5
        #         self.dice_roll -= 5
        # elif self.strength == 2 or self.strength == 3:
        #         self.attack -=4
        #         self.dice_roll -= 4
        # elif self.strength == 4 or self.strength == 5:
        #         self.attack -= 3
        #         self.dice_roll -= 3
        # elif self.strength == 6 or self.strength == 7:
        #         self.attack -=2
        #         self.dice_roll -= 2
        # elif self.strength == 8 or self.strength == 9:
        #         self.attack -= 1
        #         self.dice_roll -= 1
        # elif self.strength == 10 or self.strength == 11:
        #         self.attack
        #         self.dice_roll
        # elif self.strength == 12 or self.strength == 13:
        #         self.attack +=1
        #         self.dice_roll += 1
        # elif self.strength == 14 or self.strength == 15:
        #         self.attack += 2
        #         self.dice_roll += 2
        # elif self.strength == 16 or self.strength == 17:
        #         self.attack += 3
        #         self.dice_roll += 3
        # elif self.strength == 18 or self.strength == 19:
        #         self.attack += 4
        #         self.dice_roll += 4
        # elif self.strength == 20:
        #         self.attack += 5 * 2
        #         self.dice_roll += 5 * 2

        # if self.attack < 1:
        #     self.attack = 1

        # if   self.dexterity == 1:
        #         self.arclass -=5
        # elif self.dexterity == 2 or self.dexterity == 3:
        #         self.arclass -=4
        # elif self.dexterity == 4 or self.dexterity == 5:
        #         self.arclass -= 3
        # elif self.dexterity == 6 or self.dexterity == 7:
        #         self.arclass -=2
        # elif self.dexterity == 8 or self.dexterity == 9:
        #         self.arclass -= 1
        # elif self.dexterity == 10 or self.dexterity == 11:
        #         self.arclass
        # elif self.dexterity == 12 or self.dexterity == 13:
        #         self.arclass +=1
        # elif self.dexterity == 14 or self.dexterity == 15:
        #         self.arclass += 2
        # elif self.dexterity == 16 or self.dexterity == 17:
        #         self.arclass += 3
        # elif self.dexterity == 18 or self.dexterity == 19:
        #         self.arclass += 4
        # elif self.dexterity == 20:
        #         self.arclass += 5

        # if   self.constitution == 1:
        #         self.hitpoints -=5
        # elif self.constitution == 2 or self.constitution == 3:
        #         self.hitpoints -=4
        # elif self.constitution == 4 or self.constitution == 5:
        #         self.hitpoints -= 3
        # elif self.constitution == 6 or self.constitution == 7:
        #         self.hitpoints -=2
        # elif self.constitution == 8 or self.constitution == 9:
        #         self.hitpoints -= 1
        # elif self.constitution == 10 or self.constitution == 11:
        #         self.hitpoints
        # elif self.constitution == 12 or self.constitution == 13:
        #         self.hitpoints +=1
        # elif self.constitution == 14 or self.constitution == 15:
        #         self.hitpoints += 2
        # elif self.constitution == 16 or self.constitution == 17:
        #         self.hitpoints += 3
        # elif self.constitution == 18 or self.constitution == 19:
        #         self.hitpoints += 4
        # elif self.constitution == 20:
        #         self.hitpoints += 5
