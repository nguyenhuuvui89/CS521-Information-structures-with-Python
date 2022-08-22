"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: August 5
Homework Problem # 5_2
Description of Problem (1-2 sentence summary in your own words):
Analyze string and print out results using functions
"""
STRING = "WWWAS IT A RAT I SAW"
tmp_1 = 'The string being analyzed is: "{}"'
tmp_2 = "1. Letter counts: {}"
tmp_3 = "2. Most frequent letter '{}' appears {} times."
tmp_4 = "2. Most frequent letters: {} each appear {} times."

''' Create letter_counts function and return dictionary.'''
def letter_counts(string): 
    dict_1 = {}
    string_upper = string.upper()
    for i in string_upper:
        if i.isalpha():
            dict_1[i] = string_upper.count(i)
    return dict_1 # Return dictionary with key is letter and value is letter count.

'''Create most_common_letter function.'''
def most_common_letter(string_2): 
    dict_2 = letter_counts(string_2) # Call letter_count() function.
    most_common_letter_lst = [letter for letter in dict_2 if dict_2[letter] == max(dict_2.values())]
    return most_common_letter_lst # Return list of most common letter(s).

'''Create string_count_histogram function.'''
def string_count_histogram(string_3): 
    dict_3 = letter_counts(string_3) # Call letter_count() function.
    uniq_letter_lst = []
    for key, value in sorted(dict_3.items()):
        uniq_letter_lst.append(key*value)
    return uniq_letter_lst # Return list of unique letter.

if __name__ == '__main__':

    print(tmp_1.format(STRING))
    
    # Print Letter counts.
    dict_letter_count = letter_counts(STRING)
    dict_letter_count_lst = [f"'{key}': {dict_letter_count[key]}" for key in sorted(dict_letter_count)]
    letter_counts_formatted = ", ".join(dict_letter_count_lst)
    print(tmp_2.format(letter_counts_formatted))

    # Print most frequent letter.
    common_letter = most_common_letter(STRING)
    max_letter_appear = max(dict_letter_count.values())

    # Check to print grammatically handles.
    if len(common_letter) > 1:
        fre_letters = ", ".join([f"'{l}'" for l in sorted(common_letter)])
        print(tmp_4.format(fre_letters, max_letter_appear))
    else:
        fre_letter = common_letter[0]
        print(tmp_3.format(fre_letter,max_letter_appear))

    # Print Histogram.
    print("3. Histogram: ")
    for hist in string_count_histogram(STRING):
        print("{:3}{}".format(" ",hist))

   
