'''
In this exercise you will write a program that simulates a game of Bingo for a single card. 

Begin by generating a list of all of the valid Bingo calls (B1 through O75). 

Once the list has been created you can randomize the order of its elements by calling the shuffle function in the random module. 

Then your program should consume calls out of the list and cross out numbers on the card until the card contains a winning line. 

Simulate 1,000 games and report the minimum, maximum and average number of calls that must be made before the card wins. 

You may find it helpful to import
your solutions to Exercises "Create a Bingo Card" and "Checking for a winning Card" when completing this exercise.
'''

import random

def main_bingo():
    counter = 0
    numberofcalls = []
    randomnumber = random.sample(range(1, 76), 30)

    for num in randomnumber:
        for key in cartabingo:
            if num in cartabingo[key]:
                cartabingo[key][cartabingo[key].index(num)] = 0
    for i in range(5):
        if all([cartabingo[key][i] == 0 for key in 'BINGO']):
            bingo = True
            counter += 1
    for key in 'BINGO':
        if all([num == 0 for num in cartabingo[key]]):
            bingo = True
            counter += 1
    if cartabingo['B'][0] == 0 and cartabingo['I'][1] == 0 and cartabingo['N'][2] == 0 and cartabingo['G'][3] == 0 and cartabingo['O'][4] == 0:
        bingo = True
        counter += 1
    if cartabingo['B'][4] == 0 and cartabingo['I'][3] == 0 and cartabingo['N'][2] == 0 and cartabingo['G'][1] == 0 and cartabingo['O'][0] == 0:
        bingo = True
        counter += 1
    bingo = False
    numberofcalls.append(counter)
    return(numberofcalls)

cartabingo = {
    'B' : random.sample(range(1, 16), 5),
    'I' : random.sample(range(16, 31), 5),
    'N' : random.sample(range(31, 46), 5),
    'G' : random.sample(range(46, 61), 5),
    'O' : random.sample(range(61, 76), 5),
}

array = []
for i in range(1, 16):
    array.append(f"B{i}")
for i in range(16, 31):
    array.append(f"I{i}")
for i in range(31, 46):
    array.append(f"N{i}")
for i in range(46, 61):
    array.append(f"G{i}")
for i in range(61, 76):
    array.append(f"O{i}")
random.shuffle(array)

main_bingo()
numberofcalls = main_bingo()
print(numberofcalls)