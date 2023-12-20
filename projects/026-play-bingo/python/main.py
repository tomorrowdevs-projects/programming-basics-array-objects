from projects.checking_for_a_winning_card.python.main import winning_card, card_generate, display_card
import random


def play_bingo(card):
    bingo_calls = []
    letters = "BINGO"
    i = 16

    for letter in letters:

        for number in range(i - 15, i):
            bingo_calls.append(f"{letter}{number}")

        i += 15

    call_counter = 0
    random.shuffle(bingo_calls)

    for call in bingo_calls:
        call_counter += 1
        check_card = winning_card(card)

        if check_card:
            break
        call_number = int(call[1:])

        for key, value in card.items():

            if call_number in card[call[0]]:
                index = card[call[0]].index(call_number)
                value[index] = 0

    return call_counter


def max_min_average():
    number_of_calls = []

    for n in range(1000):
        number_of_calls.append(play_bingo(card_generate()))

    maximum = max(number_of_calls)
    minimum = min(number_of_calls)
    average = (sum(number_of_calls)) // len(number_of_calls)

    return average, minimum, maximum


def main():
    average, minimum, maximum = max_min_average()

    print(maximum, minimum, average)


if __name__ == '__main__':
    main()
