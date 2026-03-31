"""
SDEV220 M02 Lab - Case Study: if...else and while
Author: Conner Millard
File Name: student_gpa_app.py

Description:
This program accepts student names and GPAs, then determines if the student
qualifies for the Dean's List or Honor Roll based on their GPA.
"""

while True:
    # Ask for last name
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ")

    # Exit condition
    if last_name == 'ZZZ':
        print("Program terminated.")
        break

    # Ask for first name
    first_name = input("Enter student's first name: ")

    # Ask for GPA
    gpa = float(input("Enter student's GPA: "))

    # Check for Dean's List
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")

    # Check for Honor Roll
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")

    else:
        print(f"{first_name} {last_name} did not qualify for honors.")

    print()  # blank line for readability