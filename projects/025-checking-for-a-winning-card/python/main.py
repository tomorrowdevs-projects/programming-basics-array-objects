'''
A winning Bingo card contains a line of 5 numbers that have all been called. 

Players normally record the numbers that have been called by crossing them out or marking them with a Bingo dauber. 

In this exercise we will mark that a number has been
called by replacing it with a 0 in the Bingo card dictionary.

Write a function that takes a dictionary representing a Bingo card as its only
parameter. 

If the card contains a line of five zeros (vertical, horizontal or diagonal) then your function should return True, indicating that the card has won. 

Otherwise the function should return False.

Create a main program that demonstrates your function by creating several Bingo cards, displaying them, and indicating whether or not they contain a winning line. 

You should demonstrate your function with at least one card with a horizontal line, at least one card with a vertical line, at least one card with a diagonal line, and at least one card that has some numbers crossed out but does not contain a winning line. 

You will probably want to import your solution to Exercise "Create a Bingo Card" when completing this exercise.
'''

import random

array = {
    'B' : random.sample(range(1, 16), 5),
    'I' : random.sample(range(16, 31), 5),
    'N' : random.sample(range(31, 46), 5),
    'G' : random.sample(range(46, 61), 5),
    'O' : random.sample(range(61, 76), 5),
}

randomnumber = random.sample(range(1, 76), 30)

for num in randomnumber:
    for key in array:
        if num in array[key]:
            array[key][array[key].index(num)] = 0

bingo = False

for i in range(5):
    if array['B'][i] == 0 and array['I'][i] == 0 and array['N'][i] == 0 and array['G'][i] == 0 and array['O'][i] == 0:
        bingo = True

for key in array:
    if array[key][0] == 0 and array[key][1] == 0 and array[key][2] == 0 and array[key][3] == 0 and array[key][4] == 0:
        bingo = True

if array['B'][0] == 0 and array['I'][1] == 0 and array['N'][2] == 0 and array['G'][3] == 0 and array['O'][4] == 0:
    bingo = True

if array['B'][4] == 0 and array['I'][3] == 0 and array['N'][2] == 0 and array['G'][1] == 0 and array['O'][0] == 0:
    bingo = True

if bingo:
    print("!!!BINGO!!!")
else:
    print("Nessun BINGO per ora...")

for i in range(5):
    print(f"{array['B'][i]:2}  {array['I'][i]:2}  {array['N'][i]:2}  {array['G'][i]:2}  {array['O'][i]:2}")