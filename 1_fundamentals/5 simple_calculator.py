# Title: Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))

    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Get the operator from the user
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operator. Please use +, -, *, or /.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
