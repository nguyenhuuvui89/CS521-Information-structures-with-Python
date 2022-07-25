"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_3
Description of Problem (1-2 sentence summary in your own words):

"""
TEXT_FORM = "--> Error:"
while True:
    user_input = input("Please enter a 3-digit integer: ")
    if float(user_input).is_integer():
        if len(set(user_input)) != len(user_input):
            print(f"{TEXT_FORM} Your number contains duplication.")
        elif len(user_input) != 3:
            print(f"{TEXT_FORM} You did not enter a 3-digit number.")
        elif not user_input[0] < user_input[1] < user_input[2]:
            print(f"{TEXT_FORM} The digits are not in ascending order.")
        elif user_input[0] < user_input[1] < user_input[2]:
            print("Number Accepted!")
            break
    else:
        print(f"{TEXT_FORM} This is not an integer. Please re-enter.")
    