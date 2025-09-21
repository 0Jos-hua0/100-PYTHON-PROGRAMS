# Title: Conditional Statements
# This program demonstrates the use of if, elif, and else statements.

try:
    # Get a number from the user
    age = int(input("Enter your age: "))

    # Check the age and print a corresponding message
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    elif age < 13:
        print("You are a child.")
    elif age < 18:
        print("You are a teenager.")
    elif age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

except ValueError:
    print("Invalid input. Please enter a valid number for your age.")

# Example with a fixed number
number = -5

if number > 0:
    print(f"\nThe number {number} is positive.")
elif number == 0:
    print(f"\nThe number {number} is zero.")
else:
    print(f"\nThe number {number} is negative.")
