def get_multiples(n, limit):
    multiple = 0
    multiples = []

    i = 2
    while multiple < limit:
        multiple = i * n
        multiples.append(multiple)

        i += 1

    return multiples


def get_prime_numbers(limit):
    list_of_numbers = []

    for number in range(2, limit + 1):
        list_of_numbers.append(number)

    p = 2
    i = 1

    while p < limit:
        i += 1
        multiples = get_multiples(i, limit)

        for multiple in multiples:
            if multiple in list_of_numbers:
                index = list_of_numbers.index(multiple)
                list_of_numbers[index] = 0

        p += 1

    return list_of_numbers


def main():
    limit = int(input("Enter a limit: "))

    print(get_prime_numbers(limit))


if __name__ == '__main__':
    main()
