import random


def lottery_numbers():
    numbers = []

    while len(numbers) < 6:
        number = random.choice(range(1, 50))

        if number not in numbers:
            numbers.append(number)

    numbers.sort()
    return numbers
