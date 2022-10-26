class Character:
    def __init__(self, name, alignment, arclass, expoints, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.name = name
        self.alignment = alignment
        self.arclass = arclass
        self.hitpoints = 5
        self.expoints = expoints
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution 
        self.wisdom = wisdom
        self.intelligence = intelligence 
        self.charisma = charisma
        self.attack = 1
        self.is_alive = True

    def can_attack(self, dice_roll, enemy):
        if dice_roll == 20:
            self.attack += 1
        if dice_roll >= enemy.arclass:
            enemy.hitpoints -= self.attack

    def take_damage(self, dice_roll, enemy):
        if dice_roll == 20:
            self.attack *= 2
        if dice_roll >= self.arclass:
            self.hitpoints -= self.attack
        if self.hitpoints == 0:
            self.is_alive = False
    
    