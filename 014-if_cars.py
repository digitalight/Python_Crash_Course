cars = ['audi', 'bmw', 'subaru', 'honda']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Inequality
requested_topping = 'cheese'
if requested_topping != 'ham and pineapple':
    print("Hold on the Ham and Pineapple")

# Multiple Conditions
age_0 = 22
age_1 = 17
if age_0 >=18 and age_1 <18 :
    print("welcome")
else:
    print("Fail")

# Checking in list
requested_topping = ['ham', 'cheese']
if 'mushroom' not in requested_topping:
    print ("There is no mushroom in this pizza")

# Elif ticket price
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 10
else:
    price = 20
print(f"Your ticket price is £{price}")