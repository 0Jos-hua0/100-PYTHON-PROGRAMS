"""
Hello World Program (Program #1)
--------------------------------
"""

def main():
    """
    Main function that contains the program's primary functionality.
    This function prints a greeting message to the console.
    """
    # The print() function outputs text to the standard output device (screen).
    # The text to be printed is enclosed in either single (') or double (") quotes.
    print("Hello, World!")

# This block ensures the main() function runs only when the script is executed directly,
# not when it's imported as a module in another script.
if __name__ == "__main__":
    main()
    
    # Additional information for learners
    print("\nLearning Points:")
    print("1. Every Python program can contain a 'main' function as an entry point.")
    print("2. The print() function is used to display output.")
    print("3. Text in programming is called a 'string' and is enclosed in quotes.")
    print("4. The if __name__ == '__main__': block controls script execution.")
