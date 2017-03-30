#the number of cars available
cars = 100
#the number of passengers that fit into a cars
space_in_a_car = 4.0
#the number of drivers available
drivers = 30
#the number of passengers, that need to be carpooled
passengers = 90
#determines the number of cars that are not driven
cars_not_driven = cars - drivers
#determines the number of cars that are driven
cars_driven = drivers
#determines the maximum number of passengers that can be carpooled
carpool_capacity = cars_driven * space_in_a_car
#determines average number of passengers per car
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


#the error message means, that you used a variable, that you did not define earlier
