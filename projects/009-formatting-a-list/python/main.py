def formatting(list_of_strings):
    formatted_string = ""
    items_counter = 0

    for item in list_of_strings:
        items_counter += 1

        if len(list_of_strings) > 1:

            if items_counter == len(list_of_strings):
                formatted_string += item

            elif items_counter != len(list_of_strings) - 1:
                formatted_string += item + ", "

            else:
                formatted_string += item + " and "

        else:
            formatted_string += list_of_strings[0]

    return formatted_string


def main():
    list_of_strings = []

    while True:

        item = input("Enter an item or press enter to quit\n")

        if item == "":
            break
        else:
            list_of_strings.append(item)

    print(formatting(list_of_strings))


if __name__ == '__main__':
    main()
