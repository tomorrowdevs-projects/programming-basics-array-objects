def the_sieve_of_eratosthenes(limit):
    prime_numbers = []
    others = set()

    for p in range(2, limit + 1):

        if p not in others:
            prime_numbers.append(p)
            others.update(range(p * 2, limit + 1, p))

    return prime_numbers


def main():
    limit = int(input("Enter a limit: "))

    print(the_sieve_of_eratosthenes(limit))


if __name__ == '__main__':
    main()
