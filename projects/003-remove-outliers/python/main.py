"""
When analysing data collected as part of a science experiment it may be desirable to remove the most extreme values
before performing other calculations.

Write a function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the n smallest elements removed.
Then it should return the new copy of the list as the function’s only result.
The order of the elements in the returned list does not have to match the order of the elements in the original list.

Write a main program that demonstrates your function.
It should read a list of numbers from the user and remove the two largest and two smallest values from it by calling the
function described previously.
Display the list with the outliers removed, followed by the original list.

Your program should generate an appropriate error message if the user enters less than 4 values.
"""


def remove_outliers(list_of_numbers: list[int], n: int) -> list[int]:
    """
    Gets a list of numbers and removes outliers

    param list_of_numbers: list of integers
    param n: number of outliers to remove

    return: The new list without the outliers
    """

    i = list_of_numbers[0]

    while n > 0:
        for number in list_of_numbers:

            if number >= i:
                i = number

        list_of_numbers.remove(i)

        for number in list_of_numbers:

            if number <= i:
                i = number

        list_of_numbers.remove(i)

        n -= 1

    return list_of_numbers


def main():
    numbers = []

    while True:

        user_number = input("Enter a number to add in your list, or enter zero to display your list of numbers:\n")

        try:
            user_number = int(user_number)

            if user_number == 0:
                break

            else:
                numbers.append(user_number)

        except ValueError:
            print("It must to be an integer!!!")

    if len(numbers) < 4:
        raise Exception("You can't enter less than 4 values")

    print(remove_outliers(numbers, 2))


if __name__ == '__main__':
    main()