"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_3
Description of Problem (1-2 sentence summary in your own words):

"""
FIRST_NAME = ["Jane", "John"]
LAST_NAME = ["Doe", "Deer", "Black"]

if len(LAST_NAME) >= len(FIRST_NAME):
    first_name_lst = FIRST_NAME.copy()
    for i in range(len(LAST_NAME)):
        if len(FIRST_NAME) < len(LAST_NAME):
            first_name_lst.append(None)
    dict_name = dict(zip(LAST_NAME, first_name_lst))
    print(f"First Name: {FIRST_NAME}")
    print(f"Last Name: {LAST_NAME}")
    print(f"Name Dictionary: {dict_name}")
else:
    print("Error: Last name list and First name list are not same size.")


