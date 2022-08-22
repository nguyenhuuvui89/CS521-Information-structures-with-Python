"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 5
Homework Problem # 5_1
Description of Problem (1-2 sentence summary in your own words):
Create function to count vowels and consonants in file. Validate file as well
"""
tmp_1 = "Enter a text file: {}"
tmp_2 = "Total # of vowels in text file: {:,}"
tmp_3 = "Total # of consonants in text file: {:,}"

'''Create function to count vowels and consonants in file'''
def vc_counter(text_file): 
    count_dict = {}
    vowel_lst = ["A", "E", "I", "O", "U"]
    vowel_count = 0
    cons_count = 0
    with open(text_file, "r") as file: # read file.
        for line in file:
            line_upper = line.upper()
            # create list with upper letter.
            line_upper_lst = [letter for letter in line_upper if letter.isalpha()]
            # loop through list and count vowel and consonant letter.
            for letter in line_upper_lst: 
                if letter in vowel_lst:
                    vowel_count +=1
                else: 
                    cons_count +=1
        count_dict["vowels"] = vowel_count
        count_dict["consonants"] = cons_count
        return count_dict # return dictionary.

while True: # prompt and check user for text file.
    try:
        file_name = input("Enter text file name: ")
        dict_return = vc_counter(file_name) # call function.
        break
    except FileNotFoundError:
        print("Error: File is not exist.")

# print results
print (tmp_1.format(file_name))
print(tmp_2.format(dict_return["vowels"]))
print(tmp_3.format(dict_return["consonants"]))
