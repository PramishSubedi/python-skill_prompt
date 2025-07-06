formatter = "{} {} {} {}"
# Creates a string with four placeholders using curly braces. This will be used to insert values.



print(formatter.format(1, 2, 3, 4))
# Inserts the integers 1, 2, 3, and 4 into the placeholders.
# Output: 1 2 3 4

print(formatter.format("one", "two", "three", "four"))
# Inserts the strings into the placeholders.
# Output: one two three four

print(formatter.format(True, False, False, True))
# Inserts Boolean values into the placeholders.
# Output: True False False True

print(formatter.format(formatter, formatter, formatter, formatter))
# Inserts the 'formatter' string itself into the placeholders.
# So the output is the string "{} {} {} {}", repeated four times.
# Output: {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}

formatter = "{} {} {} {}"

print(formatter.format(
    "Roses are",
    "red, violets",
    "are blue,",
    "code runs true."
))
# Inserts four custom string values, each as a line argument.
# Output: Roses are red, violets are blue, code runs true.

