cars = ['ford', 'jaguar', 'honda', 'toyota', 'audi']
for car in cars:
    print(f"{car.title()} is a car company")
    print(f"and {car.title()} produces cars\n")
print("This is outside the loop\n")

#range
print("Range:")
for value in range(1,6):
    print(value)

# Even numbers
even_numbers = list(range(2,11, 2))
print(even_numbers)