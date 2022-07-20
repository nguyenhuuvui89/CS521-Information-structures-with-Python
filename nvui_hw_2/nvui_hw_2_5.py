"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 15
Homework Problem # 2_5
Description of Problem (1-2 sentence summary in your own words):
Fizz-buzz challenge.Create a for loop and while loop from 1 to 30, and print out suitable string for
each value if it is divisible by 2,3, 5 or print combination string if its divisible for more than one of these (2,3,5), otherwise (not divisble by 2,3 or 5) not print string
"""
MAXVAL = 30 # create variable name ( for loop and while loop )
for number in range(1,MAXVAL+1): # create for loop 
    string = "" # create string
    if number % 2 == 0: # If the number is divisible by 2, add the word foo to string
        string += "foo"
    if number % 3 == 0: # If the number is divisible by 3, add the word bar to string
        string += "bar"
    if number % 5 == 0: # If the number is divisible by 5, add the word baz to string
        string += "baz"
    else:
        string = string # If the number is not divisible by 2,3 or 5, not add any word
    print(f"{str(number)}: {string}") # Print number and string

print("\nCompleted for loop and process to while loop\n")

# Repeat again using a while loop

int_number = 1 # create initial number for while loop
while int_number < MAXVAL + 1: # create while loop
    string_2 = "" # create string
    if int_number % 2 == 0: # If the int_number is divisible by 2, add the word foo to string_2
        string_2 += "foo"
    if int_number % 3 == 0: # If the int_number is divisible by 3, add the word bar to string_2
        string_2 += "bar"
    if int_number % 5 == 0: # If the int_number is divisible by 5, add the word baz to string_2
        string_2 += "baz"
    else:
        string_2 = string_2 # If the int_number is not divisible by 2,3 or 5, not add any word
    print(f"{str(int_number)}: {string_2}") # Print int_number and string_2
    int_number += 1 # update initial number
