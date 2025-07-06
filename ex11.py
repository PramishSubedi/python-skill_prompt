# print("How old are you?", end=' ')
#    # Prints the question but keeps the cursor on the same line (due to end=' ')

# age = input()
#    # Waits for user to type input and stores it in the variable 'age'

# print("How tall are you?", end=' ')
#    # Same as line 1, prints without moving to a new line

# height = input()
#    # Takes input and stores in 'height'

# print("How much do you weigh?", end=' ')
#    # Asks for weight on the same line

# weight = input()
#    # Stores the input in 'weight'

# print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#    # f-string combines and displays all three inputs in one sentence


# #####What does input() do in Python?
# #>>>>>>>input() waits for the user to type something, then returns it as a string.

# #syntax:
# name = input("What's your name? ")
# #The string inside input() is shown as a prompt (so you don’t need print()).

# # other ways to use input

# #>>>convert input to numbers:
# age = int(input("Enter your age: "))  # converts input to an integer
# weight = float(input("Enter your weight in kg: "))  # converts to float

# #>>>>Combining with .strip() or .lower():
# color = input("Favorite color? ").strip().lower()
# #example>>>>
# color = input("Favorite color? ").strip().lower()

# if color == "blue":
#     print("Cool! Blue is calming.")
# elif color == "red":
#     print("Red is such a bold choice!")
# elif color == "green":
#     print("Nature lover, huh?")
# else:
#     print(f"{color.capitalize()} is a nice color!")




# #my own form:
name = input("What's your name?\n")
hobby = input("What's your favorite hobby?\n")
hours = input("How many hours a week do you do it?\n")

print(f"\nNice to meet you, {name}!")
print(f"You enjoy {hobby} for {hours} hours a day. That's awesome!")


