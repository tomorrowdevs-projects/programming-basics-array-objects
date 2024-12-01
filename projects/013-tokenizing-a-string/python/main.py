
def tokenize(user_expression):
    token_list = []
    is_prev_number = False

    for digit in user_expression:
        if digit.isnumeric():
            if is_prev_number == True:
                new_digit = prev_digit + digit
                token_list.pop()
                token_list.append(new_digit)
                prev_digit = new_digit
                    
            else:
                token_list.append(digit)
                prev_digit = digit
                is_prev_number = True
                
        elif digit == ' ':
            is_prev_number = False

        else:
            token_list.append(digit)
            is_prev_number = False
    
    return token_list

user_math = input('Insert a mathematical expression: ')

print(tokenize(user_math))