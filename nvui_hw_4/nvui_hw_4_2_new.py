
FIRST_SEN = '"WAS IT A RAT I SAW?"'
SEC_SEN = "Wwwas it a rat I saw?"
tmplt_out_1 = "The string being analyzed is: {}"
tmplt_out_2 = "1. Dictionary of letter counts: {}"
templt_out_3 = '2. Most frequent letter "{0}" appears {1} times.'
templt_out_4 = '2. Most frequent letter {0} appears {1} times.'

string_1 = {letter: FIRST_SEN.count(letter) for letter in FIRST_SEN if letter.isalpha()}
sorted_dict = {key: string_1[key] for key in sorted(string_1.keys())}

max_key = max(string_1, key =string_1.get)
max_value = max(string_1.values())

print(tmplt_out_1.format(FIRST_SEN))
print(tmplt_out_2.format(dict(sorted(string_1.items()))))
print(templt_out_3.format(max_key,max_value))


string_2 = {letter_2 : SEC_SEN.upper().count(letter_2) for letter_2 in SEC_SEN.upper() if letter_2.isalpha()}
sorted_dict_2 = {key_2 : string_2[key_2] for key_2 in sorted(string_2.keys())}
max_value_2 = max(string_2.values())

freq_lst = []
for i in string_2:
    if string_2[i] == max_value_2:
        freq_lst.append(i)

print(tmplt_out_1.format(SEC_SEN))
print(tmplt_out_2.format(sorted_dict_2))
print(templt_out_4.format(sorted(freq_lst),max_value_2))




