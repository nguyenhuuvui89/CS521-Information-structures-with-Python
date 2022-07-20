"""
Your Name: Vincent Nguyen
Class: CS 521 - Summer 2
Date: 15 Jul
Homework Problem # 2_1
Description of Problem (1-2 sentence summary in your own words):
Doing calculation through exact order and perform converting data types and print results
"""

# Prompts the user to enter a whole number
number_input = int(input("Enter a whole number from 1 to 7: "))
# perform math on the user supplied number
calculation = ((number_input*2 + 10)/2) - number_input
# print calculation output as an integer
print("The output of calculation as an integer is", int(calculation))

# Three digit number with incrementing digits
digit_1 = str(number_input)
digit_2 = str(number_input + 1)
digit_3 = str(number_input + 2)

# Concatenate three strings to be three digit number
three_digit_number_str = digit_1 + digit_2 + digit_3

# covert three digit number to integer 
three_digit_version = int(three_digit_number_str)
print("Three-digit version is", three_digit_version)

# Sum three digits and print the result
sum_three_digit = int(digit_1) + int(digit_2) + int(digit_3)
print("Sum of three digits:", sum_three_digit)

# Perform division of three-digit version and sum of three digits
division_result = three_digit_version / sum_three_digit
print("The result of division operator is", division_result) # print the result as a float

# Reprint the result of part "f" as a truncated integer
print("The result of division operator with no decimal places is", int(division_result))
