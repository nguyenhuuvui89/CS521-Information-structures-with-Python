"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 5
Homework Problem # 5_3
Description of Problem (1-2 sentence summary in your own words):
Ask for user input 4 delimited numbers and check error handlings,
perform calculation and print out result.
"""

while True:  
    inp = input("Enter four numbers separated each number by space: ") # Prompt user input.
    try:
        # Convert user input to list without space, convert string elements to integer.
        inp_lst_int = [int(i) for i in inp.split(" ")] 
        # Perform calculation.
        cal_result = ((inp_lst_int[0] * inp_lst_int[1]) + inp_lst_int[2]) / inp_lst_int[3]
        break
    except ValueError: # Handle Value Error.
        print("Error: ValueError. Try again")
    except ZeroDivisionError: # Handle Zero Division Error.
        print("Error: ZeroDivisionError. Try again")
    except IndexError: # Handle Index Error.
        print("Error: IndexError. Try again")
        
print(f"(({inp_lst_int[0]} * {inp_lst_int[1]}) + {inp_lst_int[2]}) / {inp_lst_int[3]} = {cal_result:,.2f} ")
