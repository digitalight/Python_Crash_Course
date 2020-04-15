# Slicing
players = ['charles', 'harry', 'ben', 'john', 'paul', 'vince']
print(players[0:3])
print(players[:4])
print(players[-3:])

# Looping Slices
for player in players[-3:]:
    print(player.title())

# Copying Slices
my_foods = ['pizza', 'chicken', 'pasta']
friends_foods = my_foods[:]

my_foods.append('lasagne')
friends_foods.append('curry')

print("\nMy food is:")
print(my_foods)
print("\nFriends food is:")
print(friends_foods)

# Tuple (A constant list)
print("\nTuple:")
dimensions = (200,40)
for dimension in dimensions:
    print(dimension)