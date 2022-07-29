input_list = []
new_list = []
for number in range (55, 4, -10):
    input_list.append(number)
for i in range(len(input_list)):
    if  i == 0:
        new_list.append(input_list[i] + input_list [i+1])
    elif i == len(input_list) - 1:
        new_list.append(input_list[i-1] + input_list[i])
    else:
        new_list.append(input_list[i-1] + input_list[i] + input_list[i+1])
print(f"Input List: {input_list}")
print(f"Result List: {new_list}")