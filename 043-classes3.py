from car import Car, ElectricCar as EC

# Car class output

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_description_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = EC('tesla', 'roadster', 2018)
print(my_tesla.get_description_name())