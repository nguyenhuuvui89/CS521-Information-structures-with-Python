"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_3
Description of Problem (1-2 sentence summary in your own words):
Create dictionary with key is last names and value is first names by using zip function,
add None to first name if  first name is less than last names.
"""
FIRST_NAMES = ["Jane", "John"]
LAST_NAMES = ["Doe", "Deer", "Black"]

if len(FIRST_NAMES) <= len(LAST_NAMES):  # Check if  last names same size or bigger size than first names
    first_name_lst = FIRST_NAMES.copy()
    for i in range(len(LAST_NAMES) - len(FIRST_NAMES)): # Add None if first names less than last names
            first_name_lst.append(None)
    dict_name = dict(zip(LAST_NAMES, first_name_lst)) # Create dictionary by using zip function
    print(f"First Name: {FIRST_NAMES}")
    print(f"Last Name: {LAST_NAMES}")
    print(f"Name Dictionary: {dict_name}")
else:
    print("Error: Last names list is not same size or larger than First names list ")


