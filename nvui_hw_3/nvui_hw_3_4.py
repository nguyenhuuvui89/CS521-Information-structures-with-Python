"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_4
Description of Problem (1-2 sentence summary in your own words):
read, write file and error handling
"""
# assign input and output file name to variable
FILE_INPUT_NAME = "cs521_3_4_input.txt" 
FILE_OUTPUT_NAME = "cs521_3_4_output.txt"
try: 
    input_file = open(FILE_INPUT_NAME, "r")
    output_file = open(FILE_OUTPUT_NAME, "w")
    WORDS_LIMIT = 20
    WORDS_PER_LINE = 5
    read_line = input_file.readline().strip() # read and strip the line
    read_line_lst = read_line.split(" ") # split string to get list
    if len(read_line_lst) == WORDS_LIMIT: # check if the file  == 20 words
        # loop through line list, increment by 5 (WORDS_PER_LINE) 
        for i in range(0, len(read_line_lst), WORDS_PER_LINE):  
            line_lst = read_line_lst[i:i + WORDS_PER_LINE] # Get line list with 5 elements
            line_str = " ".join(line_lst) # create string by join line list
            # write line to output_file (cs521_3_4_output.txt)
            print(line_str, file = output_file)  
        print(f"Success! Output written to: {FILE_OUTPUT_NAME}")  
        # print error message if file does not have 20 words 
    else:
        print("Error: The file has a different number of words.")   
    input_file.close()
    output_file.close()          
except FileNotFoundError:
    print("Error: file is missing") # print error if file input missing


