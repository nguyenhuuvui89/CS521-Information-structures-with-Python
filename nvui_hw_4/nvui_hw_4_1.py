"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_1
Description of Problem (1-2 sentence summary in your own words):
Create list int from 55 to 5 every 10th number.
Create new list with sum of nearest neighbors and itself
"""
START_NO = 55
STOP_NO = 5
IN_LIST = [number for number in range(START_NO, STOP_NO - 1, -10)]  # create input list form 55 to 5, every 10th number
new_list = []
for i in range(len(IN_LIST)):  # loop through input list
    # each integer is the sum of its nearest neighbors and itself from the original list.
    # begin and end only have one nearest neighbor.
    if i == 0:  # check if  first element
        new_list.append(IN_LIST[i] + IN_LIST[i + 1])
    elif i == len(IN_LIST) - 1:  # check if  last element
        new_list.append(IN_LIST[i - 1] + IN_LIST[i])
    else:
        new_list.append(IN_LIST[i - 1] + IN_LIST[i] + IN_LIST[i + 1])
# print results
print(f"Input List: {IN_LIST}")
print(f"Result List: {new_list}")
