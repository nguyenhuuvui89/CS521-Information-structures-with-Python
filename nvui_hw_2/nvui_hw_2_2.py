"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 15
Homework Problem # 2_2
Description of Problem (1-2 sentence summary in your own words):
Ask user to input a string or a number, print result as a string,  as an integer, as a floating-point value
answer question which data type can user input without getting any errors and explain why
"""
# prompt user to enter a string or a number
user_input = input("Enter a string or a number: ")
# Print the user_input 
print("user input as a string:", user_input) # print as a string (input function return a string)
print("user input as an integer:", int(user_input)) # print as an integer
print("user input as a float:", float(user_input)) # print as a floating-point value

'''
if you input an integer (int) that will print three print statements above without any errors, you can convert integer to string and float without any errors.
You will get errors if you input a string or float. Because when you input string, we will get an error if we convert user_input to integer ((ValueError: invalid literal for int() with base 10))
or to float (ValueError: could not convert string to float). You will also get error when you input a float, you will get error if you covert user_input to integer (ValueError: invalid literal for
int() with base 10).
'''

