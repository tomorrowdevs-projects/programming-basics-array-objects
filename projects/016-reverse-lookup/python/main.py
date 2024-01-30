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

        if key == "":
            break

        value = input("Enter the value associated with the key: ")

        dictionary[key] = value

    k = input("Enter the value associated with the key to find: ")

    print(reverseLookup(dictionary, k))


if __name__ == '__main__':
    main()