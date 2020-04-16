alien_0 = {'pos_x': 0, 'pos_y': 25, 'speed': 'medium', 'points': 5}
print(f"Original position: {alien_0['pos_x']}")

# Move alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_inc = 1
elif alien_0['speed'] == 'medium':
    x_inc = 2
else:
    # Must be a fast alien then
    x_inc = 3

# New position
alien_0['pos_x'] = alien_0['pos_x'] + x_inc
print(f"New position is: {alien_0['pos_x']}")


# Delete a pair
print(alien_0)
del alien_0['points']
print(alien_0)