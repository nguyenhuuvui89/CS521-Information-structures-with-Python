"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_2
Description of Problem (1-2 sentence summary in your own words):

"""
input_list = [number for number in range(55,4,-10)]  # create input list form 55 to 5, every 10th number
new_list = []
for i in range(len(input_list)): # loop through input list
    if i == 0: # check if  first element
        new_list.append(input_list[i] + input_list[i+1])
    elif i == len(input_list) - 1: # check if  last element
        new_list.append(input_list[i-1] + input_list[i])
    else:
        new_list.append(input_list[i-1] + input_list[i] + input_list[i+1])
# print results
print(f"Input List: {input_list}")
print(f"Result List: {new_list}")