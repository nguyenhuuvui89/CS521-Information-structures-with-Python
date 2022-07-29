"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_1
Description of Problem (1-2 sentence summary in your own words):
Loop through 2 - 30(inclusive), count total odd numbers, even numbers,
squares of int and cube of int. print out results.
"""
# create start and stop value for loop
START_VALUE = 2
STOP_VALUE = 130
# variable for counting odd, even, cube of int and cube of int
odd_totals = 0
odd_list = []

even_totals = 0
even_list = []

square_totals = 0
square_list = []

cube_totals = 0
cube_list = []

# create loop from 2 - 130 (inclusive)
for number in range(START_VALUE,STOP_VALUE + 1):
    if number % 2 != 0: # check and count for odd numbers
        odd_totals += 1 
        odd_list.append(number)
    if number % 2 == 0: # check and count for even numbers
        even_totals += 1
        even_list.append(number)
    if number**2 < STOP_VALUE: # check and count for square of int
        square_totals += 1
        square_list.append(number**2)
    if number**3 < STOP_VALUE:  # check and count for cube of int  
        cube_totals += 1
        cube_list.append(number**3)
# print results
print("Checking numbers from {} to {}".format(START_VALUE,STOP_VALUE))
print(f"Odd ({odd_totals}) : {odd_list[0]}...{odd_list[len(odd_list)-1]}")
print(f"Even ({even_totals}) : {even_list[0]}...{even_list[len(even_list)-1]}")
print(f"Square ({square_totals}) : {square_list}")
print(f"Cube ({cube_totals}) : {cube_list}")
