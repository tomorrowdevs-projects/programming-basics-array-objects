def numbers_in_english(int_value):
    units = {
    '0' : '',
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine'
    }
    
    tens = {
    '0' : 'and',
    '1' : 'ten',
    '2' : 'twenty',
    '3' : 'thirty',
    '4' : 'fourty',
    '5' : 'fifty',
    '6' : 'sixty',
    '7' : 'seventy',
    '8' : 'eighty',
    '9' : 'ninety'
    }

    teen_num = {
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fiveteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen'
    }
    
    english_num = []

    n_digit = len(int_value)
    if n_digit == 3:
        english_num.append(units[int_value[0]] + ' hundred')

        if int_value[1] == '1':
            english_num.append(teen_num[int_value[n_digit-2:]])

        else:
            english_num.append(tens[int_value[1]])
            english_num.append(units[int_value[2]])

    elif n_digit == 2:
        if int_value[0] == '1':
            english_num.append(teen_num[int_value[n_digit-1:]])

        else:
            english_num.append(tens[int_value[0]])
            english_num.append(units[int_value[1]])

    else:
        english_num.append(units[int_value[0]])
    
    return ' '.join(english_num)


user_input = input('Insert an integer number between 0 and 999: ')
print(numbers_in_english(user_input))

