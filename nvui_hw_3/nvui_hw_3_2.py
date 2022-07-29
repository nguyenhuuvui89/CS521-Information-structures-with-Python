"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_2
Description of Problem (1-2 sentence summary in your own words):
Create docstring with 2 sentence strings. Count uppercase letter, lowercase letters,
digits and punctuation characters. Print results neatly follow format in example. 
"""
import string

# create docstring
SENTENCES_STR = '''The rain in #Spain in 2019, rained "mainly' on the plain.
It's Featuring is #1 hybrid 2-in1 cable.
Computer can connect With the UGA-HDMI-2S'''

# create list of sentence using split function
sentence_lst = SENTENCES_STR.strip().split("\n") 

# create template for printing results
template_str = "{:^5}{:^11}{:^11}{:^11}{:^11}"

# print header of output results
print(template_str.format("#","# Upper","# Lower","# Digits","# Punct."))
print(template_str.format("-","-"*7,"-"*8,"-"*8,"-"*8))

for i in range(len(sentence_lst)): # loop through sentence_lst 
    # create counting variable for uppercase, lowercase, digits and punctuation letters
    uppercase_letter_count = 0
    lowercase_letter_count = 0
    digit_count = 0
    punctuation_count = 0
    for element in sentence_lst[i]: # loop through sentence_lst's elements
        if element in string.ascii_uppercase: # check and count for uppercase 
            uppercase_letter_count += 1
        if element in string.ascii_lowercase: # check and count for lowercase 
            lowercase_letter_count += 1
        if element in string.digits: # check and count for digits 
            digit_count += 1
        if element in string.punctuation: # check and count for punctuation characters
            punctuation_count += 1
    # print the results
    print(template_str.format(i+1,uppercase_letter_count,lowercase_letter_count,digit_count,punctuation_count))


