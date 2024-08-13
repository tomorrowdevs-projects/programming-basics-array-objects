'''
In the game of Scrabble, each letter has points associated with it. The total score of a word is the sum of the scores of its letters.

More common letters are worth fewer points while less common letters are worth more points. The points associated with
each letter are shown below:

|Points| Letters|
|------|---------|
|1| A, E, I, L, N, O, R, S, T, U|
|2| D, G|
|3| B, C, M, P|
|4| F, H, V, W, Y|
|5|K|
|8| J, X|
|10| Q, Z|

Write a program that computes and displays the Scrabble score for a word. 

Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.
'''

array = {
    'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

word = input("Please input a word: ").lower()
score = 0

for char in word:
    if char in array:
        score += array[char]
       
print(score)