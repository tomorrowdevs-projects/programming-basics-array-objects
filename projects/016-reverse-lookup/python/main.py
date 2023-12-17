def reverseLookup(dictionary, value):
    list_of_keys = []

    for key, v in dictionary.items():

        if v == value:
            list_of_keys.append(key)

    return list_of_keys


def main():
    dictionary = {}

    while True:
        key = input("Enter the key to add or press enter to quite: ")
        try:
            key = int(key)
        except ValueError:
            pass

        if key == "":
            break

        value = input("Enter the value associated with the key: ")
        try:
            value = int(value)
        except ValueError:
            pass

        dictionary[key] = value

    k = input("Enter the value associated with the key to find: ")

    print(reverseLookup(dictionary, k))


if __name__ == '__main__':
    main()