from math import pow
START_VALUE = 2
STOP_VALUE = 130
odd_totals = 0
odd_list = []
even_totals = 0
even_list = []
square_totals = 0
square_list = []
cube_totals = 0
cube_list = []
for number in range(START_VALUE,STOP_VALUE + 1):
    if number % 2 != 0:
        odd_totals += 1 
        odd_list.append(number)
    if number % 2 == 0:
        even_totals += 1
        even_list.append(number)
    if int(pow(number,2)) < STOP_VALUE:
        square_totals += 1
        square_list.append(int(pow(number,2)))
    if int(pow(number,3)) < STOP_VALUE:
        cube_totals += 1
        cube_list.append(int(pow(number,3)))
print("Checking numbers from {} to {}".format(START_VALUE,STOP_VALUE))
print(f"Odd ({odd_totals}) : {odd_list[0]}...{odd_list[len(odd_list)-1]}")
print(f"Even ({even_totals}) : {even_list[0]}...{even_list[len(even_list)-1]}")
print(f"Square ({square_totals}) : {square_list}")
print(f"Cube ({cube_totals}) : {cube_list}")