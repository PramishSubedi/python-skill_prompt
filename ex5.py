# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height= 74 # inches
# my_weight= 180 # lbs
# my_eyes = 'Blue'
# my_teeth= 'White'
# my_hair= 'Brown'

# print(f"Let's talk about {my_name}.")
# print(f"He's {my_height} inches tall.")
# print(f"He's {my_weight} pounds heavy.")
# print("Actually that's not too heavy.")
# print(f"He's got {my_eyes} eyes and {my_hair} hair.")
# print(f"His teeth are usually {my_teeth} depending on the coffee.")

# # this line is tricky, try to get it exactly right
# total = my_age + my_height + my_weight
# print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")



name = 'Pramish Subedi'
age = 21
height = 70.8661 # inches
weight = 176.37 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

# Convert height to centimeters and weight to kilograms
height_in_cm = height * 2.54  # 1 inch = 2.54 cm. >>>>>179.99 cm
weight_in_kg = weight * 0.453592 # 1 pound = 0.453592 kg. >>>>80.00 kg

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"Which is {height_in_cm:.2f} centimeters.")
print(f"He's {weight} pounds heavy.")
print(f"Which is {weight_in_kg:.2f} kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


Total = age + height_in_cm + weight_in_kg
print(f"In metric units, the total of age, height (cm), and weight (kg) is {Total:.2f}.")
