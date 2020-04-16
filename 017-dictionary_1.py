alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
new_points = alien_0['points']
print(f"You have earned {new_points} points")

# Adding to a dictionary
print(alien_0)

alien_0['pos_x'] = 0
alien_0['pos_y'] = 20

print(alien_0)

# Starting Empty
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values

alien_0['color'] =  'yellow'
print(f"The alien is now {alien_0['color']}")