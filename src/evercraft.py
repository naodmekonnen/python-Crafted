class Character:
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma, dice_roll):
        self.name = name
        self.alignment = alignment
        self.expoints = expoints
        self.strength = strength
        self.dexterity = dexterity 
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence 
        self.charisma = charisma
        self.attack = 1 + self.modifier('strength')
        self.is_alive = True
        self.dice_roll = dice_roll + self.modifier('strength')
        self.level = 1
        self.hitpoints = 5 + self.modifier('constitution')
        self.arclass = arclass + self.modifier('dexterity')

    def modifier(self, ability):
        return (getattr(self, ability) - 10)//2

    def make_attack(self, enemy):
        if self.attack < 1:
            self.attack = 1
        if self.dice_roll == 20:
            self.attack += 1
        if self.dice_roll >= enemy.arclass:
            enemy.hitpoints -= self.attack
            self.expoints += 10

    def take_damage(self, enemy):
        if self.dice_roll == 20:
            self.attack *= 2
        if self.dice_roll >= self.arclass:
            self.hitpoints -= self.attack
        if self.hitpoints == 0:
            self.is_alive = False
    
    def level_up(self):
        if self.expoints >= 1000:
                self.level += 1
                self.hitpoints +=5
                self.dice_roll +=1

class Fighter(self, Character):
    self.hitpoints = 10 + self.modifier('constitution')
    










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
    