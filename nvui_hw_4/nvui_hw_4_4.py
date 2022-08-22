"""
Vincent Nguyen
Class: CS 521 - Summer 2
Date: Jul 29
Homework Problem # 4_4
Description of Problem (1-2 sentence summary in your own words):
Working with dictionary, print out different formatted results from keys and values.
"""
MY_DICT = {"a": 15, "c": 18, "b": 20}
# create list of keys and list of values
dict_keys = list(MY_DICT.keys()) # a. get keys
dict_values = list(MY_DICT.values())
values_formatted = ", ".join(str(value) for value in dict_values)  # b. formatted comma separated

dict_items = []
for key, value in MY_DICT.items():
    element = f"{key}: {value}"  # formatted data form  keys and values
    dict_items.append(element)
items_formatted = ", ".join(dict_items)  # c. formatted data for keys and values pair

key_ordered = sorted(list(MY_DICT.items()))  # d. sorted by keys

# e. sorted by values
# create list of tuple include key (k) and value (k) and sorted
value_ordered = sorted([(v, k) for k, v in MY_DICT.items()])
format_data_lst = []
for value, key in value_ordered:  # loop through value_ordered
    data = f"{key}: {value}"
    format_data_lst.append(data)
format_data = ", ".join(format_data_lst)  # formatted data sort in values ascending order

print(f"Keys: {dict_keys}")
print(f"Values: {values_formatted}")
print(f"Key value pairs: {items_formatted}")
print(f"Key value pairs ordered by key: {key_ordered}")
print("Key value pairs ordered by value: {}".format(format_data))

