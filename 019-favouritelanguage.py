favourite_language = {
    'jen': 'python',
    'bob': 'php',
    'jack': 'pascal',
    'sue': 'python',
    'mike': 'perl',
    }
language = favourite_language['jen'].title()
print(f"Jen\'s favourite language is {language}")

# When no key and need a default

alien_0 = {'color': 'green', 'speed': 'medium'}
point_value = alien_0.get('points', 'No points avaliable')
print(point_value)

# Looping bit

for name, language in favourite_language.items():
    print(f"{name.title()}\'s favourite language is {language.title()}")

for name in favourite_language.keys():
    print(name.title())

print("\n")

friends = ['bob', 'mike']
for name in favourite_language.keys():

    if name in friends:
        language = favourite_language[name].title()
        print(f"{name.title()}, I see you love {language}")
    else:
        print(name.title())

print(f"\nSorted:")
# Sorting Dictionary

for name in sorted(favourite_language.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Just the vaules not the keys
print("\nPrinting the values:")
for language in favourite_language.values():
    print(language.title())

# And to remove duplicates we use set
print("\nNo Deplicates using set command")
for language in set(favourite_language.values()):
    print(language.title())