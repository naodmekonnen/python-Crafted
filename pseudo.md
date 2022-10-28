Pseudocode: First Iteration

## Project Requirements

- Pseudocode should follow the examples and step through each individual task.
- Code must be commented well.
- Tests should be written first, then code written to pass the tests.


## Class

1. BEGIN
2. Create a character class
3. within this class create several attributes
4. the main attributes to include:
5. Name, alignment, armor class, hit points, ability scores
6. Strength, Dexterity, Constituion, Wisdom, Intelligence, Charisma will be  hardcoded to 10 to start
7. create and name character
    8. make test testing if character class exists
    9. make character class
    10. create init function and pass attributes
    11. make test seeing if Name attribute in character class exists
    12. make name attribute 
    13. run test seeing if a name value exists
    14. make name value
15. add alignment 
    16. make test seeing if alignment exists
    17. make alignment attribute
    18. make test seeing if alignment has value
    19. add value to alignment
    20. make test attempting to pass in alignment
    21. allow alignment to be passed in
22. END

## Methods (Functions) included within the character class

1. BEGIN 
2. ability modifer
3. use the getattr() function (and // to return integers)to calculate the ability scores 
4. END

## Attack function: 

1. BEGIN
2. pass in die roll (hardcoded)
     3. Conditional: if dice roll is 20, mulitply attack score with crit modifier
     4. Conditional: if the dice roll is equal or greater than enemy armor_class, then a hit occurs
        5. one point of damage - enemies hp
        6. character gains 10 XP
    7. else no hit occurs
8. END

## Damage function
 
1. BEGIN
2. dice roll (hardcoded) to determine success of attack or defense
3. use ability modifiers to modify attributes 
4. Conditional: if attack is successful, then, take a one point hit
    5. if dice roll is greater reduce a hitpoint
    6. Conditional: if a roll is 20, damage taken is doubled
        7. multiply by critical modifier if roll is 20
    8. Conditional: if hitpoints are down to zero, the character is dead
        9. set a variable to false if hit points are 0
10. END

- level up function
1. BEGIN
    2. Conditional: if experience points are greater than 1000, increase the level by one
    3. hit points increase by 5 plus constitution modifier
4. END


## Class

1. BEGIN
2. Create a Fighter class
3. within this class create several attributes
4. make test testing if character class exists
5. make fighter class
6. inherit attributes from charcter(parent) class
7. END

### Methods
1. BEGIN
2. use super function to inherit methods from parent class
3. create an init function within this class
4. add five to hitpoints(to the base level)
5. adjusts the level_up function to add 10 hitpoints
6. add one to dice roll(attack)
7. add two to armor class 
8. END

## Class 
1. BEGIN
2. Create a Rogue class
3. within this class create several attributes
4. make test testing if character class exists
5. make rogue class
6. inherit attributes from charcter(parent) class
7. END

### Methods
1. BEGIN
2. use super function to inherit methods from parent class
3. create an init function within this class
5. 3 points of damage instead of one for a successful attack
6. 6 points per level
7. Conditional: if wisdom modifier is greater than 0, add it to armor class in addition to dexterity
8. END

## Class 
1. BEGIN
2. Create a Paladin class
3. within this class create several attributes
4. make test testing if character class exists
5. make paladin class
6. inherit attributes from charcter(parent) class
7. END

### Methods
1. BEGIN
2. use super function to inherit methods from parent class
3. create an init function within this class
4. Conditional: if enemy alignment is evil,
        - if diceroll + modifier is greater or equal to 20(critical hit), add 2 to attack, then double
        - if diceroll + modifier is greater or equal to enemy armor class
-  able to use attack roll modifier on both the roll itself and the attack itself as a bonus
     











    





















if self.attack < 1 
     self.attack = 1
---else      
----if self.strength == 1
-----dice_roll -=5
-----self.attack -= 5
----elif self.strength ==2 or ==3
-----dice_roll -=4
-----self.attack -= 4 
----elif self.strength ==4 or ==5
-----dice_roll -=3
-----self.attack -= 3 
----elif self.strength ==6 or ==7
-----dice_roll -=2
-----self.attack -= 2 
----elif self.strength ==8 or ==9
-----dice_roll -=1
-----self.attack -= 1
----elif self.strength == 10 or ==11
-----dice_roll
-----self.attack
----if self.strength ==12 or ==13
-----dice_roll +=1
-----self.attack += 1
    elif self.strength ==14 or ==15
-----dice_roll +=2
-----self.attack += 2
    elif self.strength ==16 or ==17
-----dice_roll +=3
-----self.attack += 3
    elif self.strength ==18 or ==19
-----dice_roll +=4
-----self.attack += 4
    elif self.strength == 20
-----dice_roll +=5
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


