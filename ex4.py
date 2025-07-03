cars = 100
pace_in_a_car= 4.0
drivers = 30
passengers = 90
cars_not_driven= cars- drivers
cars_driven= drivers
carpool_capacity= cars_driven # space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")





# #####################>>>>>ERROR

# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# >>>>>>we tried to use a variable called car_pool_capacity, 
# but earlier we had created a variable named carpool_capacity (no underscore between car and pool).

# Python doesn't understand car_pool_capacity because we never created that.
# So it gives an error: "name not defined" — meaning:

# to fix this just change car_pool_capacity to carpool_capacity


#################### Is it necessary to use 4.0 instead of 4?

# Not strictly necessary.
# If we use 4, Python treats it as an integer.
# If we use 4.0, Python treats it as a floating point number.
# In this case, both will work correctly since the multiplication and division will be fine with integers or floats. 
# But using 4.0 ensures accurate float results especially when dividing or expecting decimal points.



###############What is a floating point number?

# A floating point number is a number with a decimal point, like 4.0, 2.5, 0.3333.
# It is more precise for mathematical calculations involving division or fractional values.


####################

# Total number of cars available
cars = 100

# Number of seats in each car (as a float)
space_in_a_car = 4.0

# Total number of drivers available
drivers = 30

# Total number of passengers to transport
passengers = 90

# Cars that won't be driven because of lack of drivers
cars_not_driven = cars - drivers

# Cars that will be driven (equal to number of drivers)
cars_driven = drivers

# Total capacity to transport people
carpool_capacity = cars_driven * space_in_a_car

# Average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

# Print all the results
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


################# What is = called?

# = is called the assignment operator.
# It assigns the value on the right to the variable on the left.





################### What is _ called?

# _ is called an underscore.
# It's often used in variable names to simulate spaces (since spaces are not allowed in variable names).


################ calculation using variable names
x = 20
y = 10
print(x + y)        # >>>>30
print(x / y)        #>>>> 2
print(x * y)        #>>>>> 200

i = 2
print(i ** 2)       #>>>>> 4
