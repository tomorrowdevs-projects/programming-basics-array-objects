def proper_divisor(integer):
    divisors = []
    i = 1

    while i < integer:

        if integer % i == 0:
            divisors.append(i)

        i += 1

    return divisors


def perfect_numbers(number):
    divisors = proper_divisor(number)
    perfect_number = 0

    for divisor in divisors:
        perfect_number += divisor

    if number == perfect_number:
        return True

    else:
        return False


def main():
    numbers = []

    for n in range(1, 10001):
        perfect_number = perfect_numbers(n)

        if perfect_number:
            numbers.append(n)

    print(numbers)


if __name__ == '__main__':
    main()
