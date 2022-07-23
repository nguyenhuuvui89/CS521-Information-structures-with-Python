"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 23
Homework Problem # 3_2
Description of Problem (1-2 sentence summary in your own words):

"""
import string
SENTENCES_STR = '''Dock is USB-C or USB 3 -> 1 HDMI.
It's Featuring is #1 hybrid 2-in1 cable.
Computer can connect With the UGA-HDMI-2S'''
sentence_lst = SENTENCES_STR.split(".\n")
uppercase_letter_count = 0
lowercase_letter_count = 0
digit_count = 0
punctuation_count = 0
format_str = "{:^5}{:^11}{:^11}{:^11}{:^11}"
print(format_str.format("#","# Upper","# Lower","# Digits","# Punct."))
print(format_str.format("-","-"*7,"-"*8,"-"*8,"-"*8))
for i in range(len(sentence_lst)):
    uppercase_letter_count = 0
    lowercase_letter_count = 0
    digit_count = 0
    punctuation_count = 0
    for x in sentence_lst[i]:
        if x in string.ascii_uppercase:
            uppercase_letter_count += 1
        if x in string.ascii_lowercase:
            lowercase_letter_count += 1
        if x in string.digits:
            digit_count += 1
        if x in string.punctuation:
            punctuation_count += 1
    # print(f"{i+1:^11}{uppercase_letter_count:^11}{lowercase_letter_count:^11}{digit_count:^11}{punctuation_count:^11}")
    print(format_str.format(i+1,uppercase_letter_count,lowercase_letter_count,digit_count,punctuation_count))


