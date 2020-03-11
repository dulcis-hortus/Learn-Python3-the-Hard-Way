# The number of cars
cars = 100
# The number of people who can use a car
space_in_a_car = 4.00
# The number of drivers
drivers = 30
# The number of passengers
passengers = 90
# The number of cars not driven
cars_not_driven = cars - drivers
# The number of car driven
cars_driven = drivers
# The number of carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# The number of average passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
