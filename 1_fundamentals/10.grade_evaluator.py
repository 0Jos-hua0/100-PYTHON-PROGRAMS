# Title: Grade Evaluator
# This program takes a numerical score and returns the corresponding letter grade.

try:
    # Get the score from the user
    score_str = input("Enter the score (0-100): ")
    score = float(score_str)

    # Determine the grade based on the score
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
    elif score >= 90:
        grade = 'A'
        print(f"A score of {score} is a grade of {grade}.")
    elif score >= 80:
        grade = 'B'
        print(f"A score of {score} is a grade of {grade}.")
    elif score >= 70:
        grade = 'C'
        print(f"A score of {score} is a grade of {grade}.")
    elif score >= 60:
        grade = 'D'
        print(f"A score of {score} is a grade of {grade}.")
    else:
        grade = 'F'
        print(f"A score of {score} is a grade of {grade}.")

except ValueError:
    print("Invalid input. Please enter a numerical score.")
