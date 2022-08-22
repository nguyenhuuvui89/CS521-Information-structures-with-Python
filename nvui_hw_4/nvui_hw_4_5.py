"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_5
Description of Problem (1-2 sentence summary in your own words):
Check user input and convert number to text. Using dictionary with  number as keys, words as values
"""
NUMBER_DICT = {'1': 'One', '2': 'Two', '3': 'Three',
                                '4': 'Four', '5': 'Five', '6': 'Six',
                                '7': 'Seven', '8': 'Eight', '9': 'Nine',
                                '0': 'Zero', '-': 'Negative', '.': 'Point'}

while True:
    user_input = input("Enter a Number: ")
    if "," in user_input:  # Check if user input ","
        print("Please try again without entering commas.")
    elif user_input.replace("-", "").replace(".", "").isnumeric():  # check if user input is numeric
        if "-" in user_input[1:]:  # check if  "-" in user input after first element
            print('"{}" is not a valid number. Please try again'.format(user_input))
        else:
            value_lst = []
            for i in user_input:
                value_lst.append(NUMBER_DICT[i])
            text = " ".join(value_lst)
            print("As Text: {}".format(text))
            break
    else:
        print('"{}" is not a valid number. Please try again'.format(user_input))





