"""
Write a program that reads integers from the user and stores them in an array.
Use 0 as a sentinel value to mark the end of the input.
"""


def get_list() -> list[int]:
    """
    Creates a list of numbers by user input
    return: list of integers
    """
    numbers_list = []

    while True:

        user_number = input("Enter a number to add in your list, or enter zero to display your list of numbers:\n")

        try:
            user_number = int(user_number)

            if user_number == 0:
                break

            else:
                numbers_list.append(user_number)

        except ValueError:
            print("It must to be an integer!!!")

    return numbers_list


"""
Once all the values have been read your program should display them (except for the 0) in reverse order,
with one value appearing on each line.
"""


def reverse_order(numbers_list: list[int]) -> None:
    """
    Reverses a list of numbers

    param numbers_list: list of integers
    """
    numbers_list.reverse()
    [print(number) for number in numbers_list]


def main():
    numbers = get_list()
    reverse_order(numbers)


if __name__ == '__main__':
    main()
