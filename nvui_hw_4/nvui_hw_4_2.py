"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_2
Description of Problem (1-2 sentence summary in your own words):
Analysis string and store into dictionary with letter as key, number of letter as value,
find most frequently letter, and sort dictionary by alphabetic.
"""
SENTENCE = "Wwwas it a rat I saw?"
tmplt_out_1 = 'The string being analyzed is: "{}"'
tmplt_out_2 = "1. Dictionary of letter counts: {}"
tmplt_out_3 = '2. Most frequent letter {0} appears {1} times.'
tmplt_out_4 = '2. Most frequent letter "{0}" appears {1} times.'

# Create dictionary of letter as key, number of letter as value
string_dict = {letter: SENTENCE.upper().count(letter) for letter in SENTENCE.upper() if letter.isalpha()}
# Sort dictionary by key (alphabetically)
sorted_dict = {key: string_dict[key] for key in sorted(string_dict.keys())}
max_value = max(string_dict.values())  # most frequently number of letter
freq_lst = [i for i in string_dict if string_dict[i] == max_value] # Create list of frequently letter

print(tmplt_out_1.format(SENTENCE))
print(tmplt_out_2.format(sorted_dict))
if len(freq_lst) > 1:
    print(tmplt_out_3.format(sorted(freq_lst), max_value))
else:
    print(tmplt_out_4.format(freq_lst[0], max_value))




