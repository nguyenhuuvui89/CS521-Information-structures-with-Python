"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 5
Homework Problem # 5_4
Description of Problem (1-2 sentence summary in your own words):
Working with file, remove punctuation, convert words to a list and create function 
(list_to_twice_words) take list as argument return list contain only twice repeated words.
"""
import string

'''Create remove punctuation function.'''
def remove_punctuation(inp_file): 
    with open(inp_file, "r") as file: # Open read file.
        lst = []
        for line in file: # Loop through each line and remove punctuation.
            for char in string.punctuation:
                line = line.strip().replace(char, " ")
            lst_1 = [i for i in line.split(" ") if i] # Get words list of line.
            lst.extend(lst_1) # Get words list of whole file.
        return lst

'''Create list_to_twice_words function that takes a list as an argument.'''
def list_to_twice_words(list): 
    twice_words_lst = []
    # Loop through list and get list of words repeated twice.
    for word in list: 
        if list.count(word) == 2 and word not in twice_words_lst:
            twice_words_lst.append(word)
    return twice_words_lst

# Prompt user for file name and handle error.
while True:
    inp_file_i = input("Enter your file name: ") 
    try:
        # Call remove_punctuation function return list
        inp_file_lst = remove_punctuation(inp_file_i)
        break
    except FileNotFoundError:
        print("Error: File is not exist. Try again")

# Call list_to_twice_words function and argument is list
twice_words = list_to_twice_words(inp_file_lst) 
# Print results.
print(f"List of words occurred exactly twice in the file: {twice_words}")

