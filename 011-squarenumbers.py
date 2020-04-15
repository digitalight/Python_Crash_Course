squares = []
for value in range(1,13):
    square = value ** 2
    squares.append(square)
print(squares)


# Shorter version (List Comprehensions)
squares = [value**2 for value in range(1,13)]
print(squares)