import random


def card_generate():
    card = "BINGO"
    my_dict = {}

    for letter in card:
        my_dict[letter] = []

    start = 1
    stop = 16

    for letter in card:

        while len(my_dict[letter]) < 5:
            number = random.choice([i for i in range(start, stop)])

            if number not in my_dict[letter]:
                my_dict[letter].append(number)

        start += 15
        stop += 15

    return my_dict


def main():
    card = card_generate()

    for number in range(5):

        for key, value in card.items():
            value.sort()
            print(f"{value[number]: <4}", end="")
        print()


if __name__ == '__main__':
    main()
