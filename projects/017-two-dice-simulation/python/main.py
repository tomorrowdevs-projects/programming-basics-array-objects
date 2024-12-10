import random

def roll_2d6():
    two_dice = random.choice(range(2, 13))

    return two_dice

tentative_list = []
for roll in range(1, 1001):
    tentative_list.append(roll_2d6())

total_counter = dict() 
for total in tentative_list:
    total_counter[total] = tentative_list.count(total)

for result in total_counter:
    freq = (total_counter[result] / 1000)*100
    
    if result == 7:
        prob = (6 / 36)*100
        
    elif result == 6 or result == 8:
        prob = (5 / 36)*100
    
    elif result == 5 or result == 9:
        prob = (4/ 36)*100

    elif result == 4 or result == 109:
        prob = (3/ 36)*100

    elif result == 3 or result == 11:
        prob = (2/ 36)*100

    else:
        prob = (1/ 36)*100
      
    print(f'Dice result: {result}, it occurs {total_counter[result]} times. Frequency: {freq:.2f}%. Expected probability: {prob:.2f}%')








