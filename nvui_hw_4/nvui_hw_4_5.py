DICT = {'1': 'One', '2': 'Two', '3': 'Three',
                '4': 'Four', '5': 'Five', '6': 'Six',
                '7': 'Seven', '8': 'Eight', '9': 'Nine',
                '0': 'Zero', '-': 'Negative', '.': 'Point'}

while True:
    user_input = input("Enter a Number: ")
    if "," in user_input:
        print("Please try again without entering commas.")
    elif (user_input.isalnum()) and (not user_input.isnumeric()) or " " in user_input:
        print('"{}" is not a valid number. Please try again'.format(user_input))
    else:
        value_lst = []
        for i in user_input:
           value_lst.append(DICT[i])
        text = " ".join(value_lst)
        print("As Text: {}".format(text))
        break





