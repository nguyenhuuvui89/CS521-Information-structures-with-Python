SENTENCE_STR = '"WAS IT A RAT I SAW?"'
SENTENCE_STR2 = "Wwwas it a rat I saw?"
tmp_1 = "The string being analyzed is: {}"
tmp_2 = "1. Dictionary of letter counts: {}"
tmp_3 = "2. Most frequent letter {0} appears {1} times."
count_dict = {}
for letter in SENTENCE_STR:
    if  letter.isalpha():
        count_dict[letter] = SENTENCE_STR.count(letter)

values_lst = list(count_dict.values())
keys_lst = list(count_dict.keys())
freq_time = max(values_lst)
freq_letter = keys_lst[values_lst.index(max(values_lst))]

print(tmp_1.format(SENTENCE_STR))
print(tmp_2.format(dict(sorted(count_dict.items()))))
print(tmp_3.format(freq_letter,freq_time))
# step "b"

count_dict2 ={}
sen_lst = [letter_2.upper() for letter_2 in SENTENCE_STR2 if letter_2.isalpha()]
freq_letter_lst = []
for element in sen_lst:
    count_dict2[element] = sen_lst.count(element)

values_lst2 = list(count_dict2.values())
key_lst2 = list(count_dict2.keys())
freq_time2 = max(values_lst2)

for i in range(len(values_lst2)):
    if values_lst2[i] == freq_time2:
        freq_letter_lst.append(key_lst2[i])

print(tmp_1.format(SENTENCE_STR2))
print(tmp_2.format(dict(sorted(count_dict2.items()))))
print(tmp_3.format(sorted(freq_letter_lst),freq_time2))




