need class named Character
--within class we need several attributes
--main attributes to include
---Name, alignment, armor class, hit points, ability scores
----ability scores
-----Strength, Dexterity, Constituion, Wisdom, Intelligence, Charisma (hardcoded at 10)
---total XP

--main methods to include

---ability modifer
---if self.attack < 1 
        self.attack = 1
---else      
----if self.strength == 1
-----self.attack -= 5
----elif self.strength ==2 or ==3
-----self.attack -= 4 
----elif self.strength ==4 or ==5
-----self.attack -= 3 
----elif self.strength ==6 or ==7
-----self.attack -= 2 
----elif self.strength ==8 or ==9
-----self.attack -= 1
----elif self.strength == 10 or ==11
-----self.attack
----if self.strength ==12 or ==13
-----self.attack += 1
    elif self.strength ==14 or ==15
-----self.attack += 2
    elif self.strength ==16 or ==17
-----self.attack += 3
    elif self.strength ==18 or ==19
-----self.attack += 4
    elif self.strength == 20
-----self.attack += 5

----SAME FOR CONSTITUTION

----if self.dexterity == 1
-----self.arclass -= 5
----elif self.dexterity ==2 or ==3
-----self.arclass -= 4 
----elif self.dexterity ==4 or ==5
-----self.arclass -= 3 
----elif self.dexterity ==6 or ==7
-----self.arclass -= 2 
----elif self.dexterity ==8 or ==9
-----self.arclass -= 1
----elif self.dexterity == 10 or ==11
-----self.arclass 
----elif self.dexterity ==12 or ==13
-----self.arclass += 1
----elif self.dexterity ==14 or ==15
-----self.arclass += 2
----elif self.dexterity ==16 or ==17
-----self.arclass += 3
----elif self.dexterity ==18 or ==19
-----self.arclass += 4
----elif self.dexterity ==20
-----self.arclass += 5








---Character can attack(attack method)
----pass in die roll (hardcoded)
----if the roll is >= the enemies AC then successfull hit occurs
-----one point of damage - enemies hp
-----character gains 10 XP
----else no hit occurs

---Character can take damage
----if the roll >= characters AC then character takes 1 point of damage 
----if characters hit points is == 0, character is dead
---dice roll (hardcoded) to determine success of attack or defense
---Ability Modifiers to modify attributes 



create and name character
    make test testing if character class exists
    make character class
    make test seeing if Name attribute in character class exists
    make name attribute 
    run test seeing if a name value exists
    make name value

add alignment 
    make test seeing if alignment exists
    make alignment attribute
    make test seeing if alignment has value
    add value to alignment
    make test attempting to pass in alignment
    allow alignment to be passed in

    

