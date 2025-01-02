import random
import copy

def create_bingo_card():
    bingo_card = {}
    step = 0
    for char in 'BINGO':
        bingo_card.update({char : random.sample(range(1+step, 15+step), k = 5)})
        step += 15
    return bingo_card

def display_card(dict_card):
    print('{:^3} {:^3} {:^3} {:^3} {:^3}'.format('B', 'I', 'N', 'G', 'O'))
    for i in range(0,5):
        row = list(item[i] 
                    for item in dict_card.values())
        print('{:^3} {:^3} {:^3} {:^3} {:^3}'.format(row[0], row[1], row[2], row[3], row[4]))

def check_card(dict_card):
    is_win = False
    # check columns
    for n_column in dict_card.values():
        if is_win:
            break
        else:
            for c in n_column:
                if c == 0:
                    is_win = True
                else:
                    is_win = False
                    break
    # check rows
    if not is_win:
        for i in range(len(dict_card.keys())):
            if is_win:
                break
            else:
                n_row = list(item[i] 
                            for item in dict_card.values())
                for r in n_row:
                    if r == 0:
                        is_win = True
                    else:
                        is_win = False
                        break
    # check diagonals
    if not is_win:
        diagonal_1 = dict_card['B'][0], dict_card['I'][1], dict_card['N'][2], dict_card['G'][3], dict_card['O'][4]
        for d in diagonal_1:
            if d == 0:
                is_win = True
            else:
                is_win = False    
                diagonal_2 = dict_card['B'][4], dict_card['I'][3], dict_card['N'][2], dict_card['G'][1], dict_card['O'][0]
                for d in diagonal_2:
                    if d == 0:
                        is_win = True
                    else:
                        is_win = False
                        break
                break    
    return is_win

def cross_num(dict_card, called_num):
    for list_num in dict_card.values():
        for n in range(len(list_num)):
            if list_num[n] == called_num:
                list_num[n] = 0
                break
    return dict_card

my_bingo_card = create_bingo_card()
copy_card = copy.deepcopy(my_bingo_card)
calls_list = []

for g in range(0, 1000):
    numbers_list = random.sample(range(1,76), k=75)
    call = random.choice(numbers_list)
    calls_ingame = 1
    numbers_list.remove(call)
    crossed_card = cross_num(copy_card, call)
    is_card_win = check_card(crossed_card)

    while is_card_win == False:
        call = random.choice(numbers_list)
        calls_ingame += 1
        numbers_list.remove(call)
        cross_num(crossed_card, call)
        is_card_win = check_card(crossed_card)
    
    copy_card = copy.deepcopy(my_bingo_card)
    calls_list.append(calls_ingame)    

minimum = min(calls_list)
maximum = max(calls_list)
avarage = sum(calls_list)/len(calls_list)

print(f'The minimum number of calls for the win is: {minimum}')
print(f'The maximum number of calls for the win is: {maximum}')
print(f'The avarage number of calls for the win is: {int(avarage)}')

