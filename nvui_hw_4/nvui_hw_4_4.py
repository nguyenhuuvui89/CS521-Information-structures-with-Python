MY_DICT = {"a": 15, "c": 18, "b": 20}
# create list of keys and list of values
dict_keys = list(MY_DICT.keys())
dict_values = list(sorted(MY_DICT.values()))
values_formatted = ", ".join(str(value) for value in dict_values)  # formatted comma separated

dict_items = []
for key, value in MY_DICT.items():
    element = f"{key}: {value}"  # formatted data form  key and value
    dict_items.append(element)
items_formatted = ", ".join(dict_items)  # formatted data for keys and values pair

key_ordered = sorted(MY_DICT.items())  # sorting key

value_ordered = {}
for val in  sorted(MY_DICT, key = MY_DICT.get):  # loop through sorted dict by value
    value_ordered[val] = MY_DICT[val]

format_data_lst = []
for key, value in value_ordered.items():  # loop through value_ordered (sorted dict by value)
    data = f"{key}: {value}"
    format_data_lst.append(data)
format_data = ", ".join(format_data_lst)  # formatted data sort in value ascending order

print(f"Keys: {dict_keys}")
print(f"Values: {values_formatted}")
print(f"Key value pairs: {items_formatted}")
print(f"Key value pairs ordered by key: {key_ordered}")
print("Key value pairs ordered by value: {}".format(format_data))

