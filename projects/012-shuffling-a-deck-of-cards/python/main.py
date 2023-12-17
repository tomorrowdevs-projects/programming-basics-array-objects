"""
Begin by writing a function named createDeck.
It will use loops to create a complete deck of cards by storing the two-character abbreviations for all 52 cards into
a list.
Return the list of cards as the function’s only result. Your function will not require any parameters.
"""
import random


def createDeck():
    deck = []

    for letter in ("s", "h", "d", "c"):

        for number in range(1, 14):

            if number == 1:
                deck.append(f"A{letter}")

            elif number == 10:
                deck.append(f"T{letter}")

            elif number == 11:
                deck.append(f"J{letter}")

            elif number == 12:
                deck.append(f"Q{letter}")

            elif number == 13:
                deck.append(f"K{letter}")

            else:
                deck.append(f"{number}{letter}")

    return deck


"""
Write a second function named shuffle that randomizes the order of the cards in a list. 
One technique that can be used to shuffle the cards is to visit each element in the list and swap it with another 
random element in the list. 
You must write your own loop for shuffling the cards. 
You cannot make use of a shuffle function. 
Use both of the functions described in the previous paragraphs to create a main program that displays a deck of cards 
before and after it has been shuffled. 
Ensure that your main program only runs when your functions have not been imported into another file.
"""


def shuffle(deck):
    shuffled_deck = []

    for card in deck:
        shuffled_deck.append(random.choice(deck))

    return shuffled_deck


def main():
    deck = createDeck()

    print(f"Here the sorted deck:\n{deck}\n")
    print(f"And here the shuffled deck:\n{shuffle(deck)}")


if __name__ == '__main__':
    main()
