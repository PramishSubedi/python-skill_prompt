print("Mary had a little lamb.")
# Prints a simple sentence.

print("Its fleece was white as {}.".format('snow'))
# Uses the format() method to insert 'snow' into the string.

print("And everywhere that Mary went.")
# Prints another sentence.

print("." * 10)  # what'd that do?
# Prints 10 periods in a row: ".........."
# The `*` operator repeats the string 10 times.

##Now assigning letters to build a compound word:
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# Lines 6–17 assign each character of the words "Cheese" and "Burger" to variables.


##Printing the combined words:

print(end1 + end2 + end3 + end4 + end5 + end6)
# Combines letters C-h-e-e-s-e into "Cheese"
# `end=' '` means print a space instead of a newline at the end of the line,
# so the next print() continues on the same line.

print(end7 + end8 + end9 + end10 + end11 + end12)
# Combines letters B-u-r-g-e-r into "Burger"
# Because of the space from the previous line, this prints "Cheese Burger"


