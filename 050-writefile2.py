filename = 'text_files/write2.txt'

# Make a dice class

from random import randint
class Die:
    """A Simple Dice object"""
    
    def __init__(self,sides=6):
        """Initialize name and sides of dice"""
        self.sides = sides
    def roll_die(self):
        return(randint(1,self.sides))

# Make new 6 sided die

new_die = Die()
turn = 0

# Roll the dice and write the turn into a file. Amend the file and do it 100 times.

with open(filename, 'a') as file_object:
    while turn < 100:
        file_object.write(str(new_die.roll_die()))
        turn += 1