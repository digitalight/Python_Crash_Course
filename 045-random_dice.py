# Exercise to make a dice roll 10 times. By default it is a 6 sided die.

from random import randint
class Die:
    """A Simple Dice object"""
    
    def __init__(self,sides=6):
        """Initialize name and sides of dice"""
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))

new_die = Die()
turn = 0
while turn < 10:
    new_die.roll_die()
    turn += 1
