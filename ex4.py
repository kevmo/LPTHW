cars = 100
space = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space
avg_passenger_per_car = passengers/cars_driven


print "There are ", cars, ' cars available'
print "There are only ", drivers, 'available'
print "string plus ", cars, ' works'
print "we can transport ", carpool_capacity, " today"