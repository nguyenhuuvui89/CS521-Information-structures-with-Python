"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_5
Description of Problem (1-2 sentence summary in your own words):
Read the file, print the content (parse data to a 3 objects tuple 
from each line, create list which include all tuple.
"""
FILE_INPUT_NAME = "cs521_3_5_input.txt"
with open(FILE_INPUT_NAME, "r") as file: # open file with read mode
    students_record_lst = []
    for line in file: # loop through file
        # create list 
        line_read = line.strip()
        line_lst = line_read.split(",")
        line_lst[0] = str(line_lst[0].strip())
        line_lst[1] = int(line_lst[1])
        line_lst[2] = float(line_lst[2])
        line_tuple = tuple(line_lst) # convert list to tuple
        students_record_lst.append(line_tuple) # append tuple to student record list list
    print(f"Student Records: {students_record_lst}") # print result

    
 
