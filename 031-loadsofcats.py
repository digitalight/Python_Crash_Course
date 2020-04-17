pets = ['dog', 'fish', 'cat', 'cat', 'rabbit', 'cat']
print(pets)

# Use while loop and not a for loop as they can't track lists or dictionaries.

while 'cat' in pets:
    pets.remove('cat')
print(pets)