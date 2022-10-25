class Character:
    def __init__(self, name, alignment, arclass, hitpoints, expoints):
        self.name = name
        self.alignment = alignment
        self.arclass = arclass
        self.hitpoints = hitpoints
        self.expoints = expoints
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10 
        self.wisdom = 10
        self.intelligence = 10 
        self.charisma = 10
        self.attack = 1

    def modifier(self, strmod):
        self.attack += strmod
    