import random

from projects.create_a_bingo_card.python.main import display_card, card_generate


def winning_card(dictionary):
    index = {}
    result = False

    for key, value in dictionary.items():
        horizontal = 0
        i = 0
        index[f"{key} index"] = []

        for v in value:

            if v == 0:
                horizontal += 1

                index[f"{key} index"].append(i)

                if horizontal == 5:
                    print(f"Line {key} won")
                    result = True

            i += 1

    right_diagonal = 0
    left_diagonal = 4
    vertical = 0

    for k, values in index.items():

        if right_diagonal in index[k]:

            if right_diagonal == 4:
                print("diagonal won")
                result = True

            right_diagonal += 1

        if left_diagonal in index[k]:

            if left_diagonal == 0:
                print("diagonal won")
                result = True

            left_diagonal -= 1

    for n in range(5):
        i = 0

        for k, values in index.items():

            if vertical in values:
                i += 1
                if i == 5:
                    print("vertical won")
                    result = True

        vertical += 1

    return result


def main():
    # horizontal
    horiz_win = card_generate()
    for key, value in horiz_win.items():
        value[2] = 0
    print(display_card(horiz_win))
    print(winning_card(horiz_win))

    # vertical
    vertical_win = card_generate()
    vertical_win["B"] = [0, 0, 0, 0, 0]
    print(display_card(vertical_win))
    print(winning_card(vertical_win))

    # diagonal
    diagonal_win = card_generate()
    i = 4

    for key, value in diagonal_win.items():
        value[i] = 0
        i -= 1
    print(display_card(diagonal_win))
    print(winning_card(diagonal_win))

    losing_card = card_generate()
    for key, value in losing_card.items():
        value[random.choice(range(4))] = 0
    print(display_card(losing_card))
    print(winning_card(losing_card))


if __name__ == '__main__':
    main()
