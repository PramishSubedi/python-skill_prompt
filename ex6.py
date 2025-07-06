###### >>>>>>>>>>    STRING AND TEXT

# Assigns the integer 10 to the variable 'types_of_people'
types_of_people = 10           

# A formatted string that includes 'types_of_people' inside it
x = f"There are {types_of_people} types of people."  
                                  

# Assigns the string "binary" to the variable 'binary'
binary = "binary"    

# Assigns the string "don't" to the variable 'do_not'
do_not = "don't"               

# Assigns the string "don't" to the variable 'do_not'
y = f"Those who know {binary} and those who {do_not}."


# Prints the string stored in variable 'x'
print(x)         

# Prints the string stored in variable 'y'
print(y)                      


# Prints a string that includes variable 'x' (a string inside a string)
print(f"I said: {x}")     

# Prints a string that includes variable 'y', with single quotes around it

print(f"I also said: '{y}'")   

 # Assigns the Boolean value False to the variable 'hilarious'
hilarious = False       

# A string with a placeholder for formatting
joke_evaluation = "Isn't that joke so funny?! {}"  

# Replaces {} in the string with the value of 'hilarious' (False)
print(joke_evaluation.format(hilarious))  



# Assigns a string to variable 'w'
w = "This is the left side of..."    

# Assigns a string to variable 'e'
e = "a string with a right side." 

# Concatenates 'w' and 'e' using + and prints the result
print(w + e)                          



#########Where Is a String Put Inside a String?

#1> Line 7:
x = f"There are {types_of_people} types of people."

#2> Line 17:
y = f"Those who know {binary} and those who {do_not}."

#3> Line 28:
print(f"I said: {x}")

#4> Line 32:
print(f"I also said: '{y}'")

#5> Line 41:
print(joke_evaluation.format(hilarious))

############# >>>>>So, technically there are five places where string is inserted into a string.


############Why Does w + e Make a Longer String?

"This is" + " cool"
#becomes
"This is cool"
#so in line 52:
print(w + e)
#combines
"This is the left side of..."
#and
"a string with a right side."
#into
#>>>>>>This is the left side of...a string with a right side.



