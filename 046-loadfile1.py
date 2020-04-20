# Read all of a file and print it

with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# Reading each line at a time

filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing the lines for later use as can only be access within the 'with' at this point

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

