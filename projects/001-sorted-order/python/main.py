"""
Write a program that reads integers from the user and stores them in an array.
Your program should continue reading values until the user enters 0.
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
Then it should display all of the values entered by the user (except for the 0) in ascending order, with one value
appearing on each line.
Use either the sort method or the sorted function to sort the array.
"""


def sorted_order(numbers) -> None:
    """
    Sorts the list of user numbers

    param numbers: a list of integers
    return: display on the screen the numbers in ascending order
    """
    numbers.sort()
    [print(number) for number in numbers]


def main():
    numbers = get_list()
    sorted_order(numbers)


if __name__ == '__main__':
    main()