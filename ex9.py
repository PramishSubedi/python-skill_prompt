# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"  
# Stores the days of the week in a single string, separated by spaces.

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# Stores the months in a string, each separated by newline \n so they print on new lines.

print("Here are the days: ", days)
# Prints a message and the value of the 'days' string.

print("Here are the months: ", months)
# Prints a message and the value of the 'months' string — will appear vertically because of \n.

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# This is a multi-line string enclosed in triple double-quotes.
# It prints everything inside, across multiple lines as written.
# We don't need to use \n to create line breaks — each new line inside the quotes is preserved.