# Title: Temperature Converter
# This program converts temperatures between Celsius and Fahrenheit.

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

try:
    choice = input("Choose an option (1 or 2): ")

    if choice in ('1', '2'):
        temp_str = input("Enter the temperature to convert: ")
        temp = float(temp_str)

        if choice == '1':
            converted_temp = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {converted_temp:.2f}°F")
        elif choice == '2':
            converted_temp = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {converted_temp:.2f}°C")
    else:
        print("Invalid option. Please choose 1 or 2.")

except ValueError:
    print("Invalid temperature. Please enter a number.")
