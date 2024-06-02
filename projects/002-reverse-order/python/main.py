number=input('Please enter an integer:')
number_list=list()
while number!='0':
    if number.isdecimal():
        number_list.append(number)
        number=input('Please enter an integer or enter 0 to print all the previous values:')
    else:
        number=input('You have entered a wrong value, please enter an integer or enter 0 to print all the previous values:')
number_list.reverse()
for number in number_list:
    print(number)