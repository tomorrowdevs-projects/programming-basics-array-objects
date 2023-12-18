def english_word(integer):
    total = ""
    integer = str(integer)
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
               "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    ten_multiples = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    my_dict = {}

    for number in range(1, 20):
        my_dict[number] = numbers[number - 1]

    for number in range(20, 91, 10):
        my_dict[number] = ten_multiples[(number // 10) - 2]

    if len(integer) == 1:
        total = my_dict[int(integer)]

    if len(integer) == 2 and int(integer) in my_dict:
        total = my_dict[int(integer)]

    elif len(integer) == 2:
        rest = int(integer) % 10
        total = my_dict[(int(integer) // 10) * 10] + " " + my_dict[rest]

    if len(integer) == 3:
        total = my_dict[int(integer[0])] + " " + "hundred" + " "
        integer = int(integer) % 100

        if integer > 0:

            if integer in my_dict:
                total += my_dict[integer]

            else:
                rest = integer % 10
                integer = integer - rest
                total += my_dict[integer] + " " + my_dict[rest]

    return total


def main():
    user_number = input("Enter a number between 0 and 999: ")

    while True:

        try:
            user_number = int(user_number)
            if user_number in range(0, 1000):
                print(english_word(user_number))
                break

            else:
                print("You must to enter an integer between 0 and 999!")
                user_number = input("Enter a number between 0 and 999: ")

        except ValueError:
            print("You must to enter an integer between 0 and 999!")
            user_number = input("Enter a number between 0 and 999: ")


if __name__ == '__main__':
    main()
