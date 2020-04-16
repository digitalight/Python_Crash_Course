alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# using range to make loads

humans = []

# make 30 humans
for human_number in range(30):
    new_human = {'color': 'brown', 'health': 10, 'speed': 'slow'}
    humans.append(new_human)

    # show first 5 humans
for human in humans[:5]:
    print(human)
print("...")
# Show how many humans we have
print(f"Total number of humans: {len(humans)}")