def proper_divisor(integer):
    divisors = []
    i = 1

    while i < integer:

        if integer % i == 0:
            divisors.append(i)

        i += 1

    return divisors


def main():
    user_integer = int(input("Enter an integer:\n"))

    print(f"The divisors of {user_integer} are: {proper_divisor(user_integer)}")


if __name__ == '__main__':
    main()
