# This will produce an error
# print(5/0)

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")