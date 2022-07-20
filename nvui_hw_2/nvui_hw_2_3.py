"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 15
Homework Problem # 2_3
Description of Problem (1-2 sentence summary in your own words):
Ask user to input number, perform the math and print result limit with 2 decimal places
"""

# Ask the user to enter a number
user_input = int(input("Please enter a number: "))
# Compute value from formula
computed_value = user_input**3 / user_input
# Limited result to 2 decimal places
result = "{0:.2f}".format(computed_value)
# Print formula and result
output = f"{user_input}**3/{user_input} = {result}" 
print(output)
