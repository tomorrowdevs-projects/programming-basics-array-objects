"""
In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that simulates rolling a pair
of six-sided dice. Your function will not take any parameters. It will return the total that was rolled on two dice
as its only result.

Write a main program that uses your function to simulate rolling two six-sided dice 1,000 times.
As your program runs, it should count the number of times that each total occurs.

Then it should display a table that summarizes this data.
Express the frequency for each total as a percentage of the number of rolls performed.
Your program should also display the percentage expected by probability theory for each total.
"""
import random
from tabulate import tabulate


def two_dice():
    return random.choice(range(2, 13))


def main():
    dice = {
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0
    }
    line = ["Percentage %"]
    probability = ["Dice roll probability", "1/36", "2/36", "3/36", "4/36", "5/36", "6/36", "5/36", "4/36", "3/36",
                   "2/36", "1/36"]
    for number in range(0, 1001):
        total_dice = two_dice()
        dice[total_dice] = dice[total_dice] + 1

    for key in dice:
        line.append(f"{((dice[key] / 1000) * 100):.2f}")

    data = [
        line,
        probability
    ]

    head = ["Total number rolled", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    table = tabulate(data, headers=head, tablefmt="grid")
    print(table)


if __name__ == '__main__':
    main()
