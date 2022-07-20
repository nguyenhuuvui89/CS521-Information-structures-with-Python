"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 15
Homework Problem # 2_4
Description of Problem (1-2 sentence summary in your own words):
Check even and odd number from input number in three lines program
"""
# Ask user to enter a number
user_input = input("Enter a number: ")
# Convert the input number to integer
user_input_int = int(user_input)
# Divide user_input by two and check the remainder (Modulo operator).
# number_output will be 0 if user_input is even and 1 if user_input is odd
# Print out the result 
print(user_input_int % 2 != 0 and f"Input number ({user_input_int}) is odd and the number (remainder): {user_input_int % 2}" or f"Input number ({user_input_int}) is even and the number (remainder): {user_input_int % 2}")
