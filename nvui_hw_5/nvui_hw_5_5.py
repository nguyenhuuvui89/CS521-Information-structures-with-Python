"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 5
Homework Problem # 5_5
Description of Problem (1-2 sentence summary in your own words):
Practice recursion in function using factorials.
"""
# Prompt for user input and check validation.
while True:
    try:
        inp_number = int(input("Enter factorial starting int: "))
        break
    except ValueError:
        print("Not valid number. Try again")
        
'''Create factorial function with recursion.'''
def factorial(n):
    if n == 0 or n == 1: # Base case.
        return 1
    else:
        value = n*factorial(n-1) # Recursion case.
        return value

'''Create factorial function without recursion.'''
def factorial2(n):
    START = 1
    new_value = 1
    for i in range(START, n+1):
        new_value *=i
    return new_value

# Call functions.
fact_recursion = factorial(inp_number)
fact_no_recursion = factorial2(inp_number)

# Print results.
print("Calculate factorial with recursion: {:,}".format(fact_recursion))
print("Calculate factorial without recursion: {:,}".format(fact_no_recursion))
