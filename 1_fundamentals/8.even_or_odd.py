# Title: Even or Odd Checker
# This program checks if a number entered by the user is even or odd.

try:
    # Get an integer from the user
    number = int(input("Enter a whole number: "))

    # Check if the number is divisible by 2 with no remainder
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

except ValueError:
    print("Invalid input. Please enter a valid whole number.")
