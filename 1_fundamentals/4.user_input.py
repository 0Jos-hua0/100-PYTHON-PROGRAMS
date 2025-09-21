# Title: User Input in Python
# This program demonstrates how to get input from the user.

# Get the user's name
name = input("Please enter your name: ")

# Get the user's age
age_str = input("Please enter your age: ")

# The input() function returns a string, so we need to convert the age to an integer
# to perform numerical operations.
try:
    age = int(age_str)
    # Print a personalized greeting
    print(f"Hello, {name}! You are {age} years old.")

    # You can now use the 'age' variable as a number
    print(f"In 5 years, you will be {age + 5} years old.")

except ValueError:
    print(f"Hello, {name}! That's not a valid age. Please enter a number next time.")
