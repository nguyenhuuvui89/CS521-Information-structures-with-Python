"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_3
Description of Problem (1-2 sentence summary in your own words):
Prompt user to input 3-digit number in ascending order. Check number and print accept if number correct
or error message if number is duplicate, not 3-digit number, not int, not in ascending order.
"""
from sys import exit
TEXT_FORM = "--> Error:"
while True: # create loop
    user_input = input("Please enter a 3-digit integer: ") # Prompt user
    if float(user_input).is_integer():  # check if user input is integer
        if len(set(user_input)) != len(user_input): # check duplication
            print(f"{TEXT_FORM} Your number contains duplication.")
        elif len(user_input) != 3: # check 3-digit number or not
            print(f"{TEXT_FORM} You did not enter a 3-digit number.")
        # check ascending order
        else:
            if not user_input[0] < user_input[1] < user_input[2]: 
                print(f"{TEXT_FORM} The digits are not in ascending order.")
            else: 
                print("Number Accepted!")
                exit()
    else:
        print(f"{TEXT_FORM} This is not an integer. Please re-enter.")
    