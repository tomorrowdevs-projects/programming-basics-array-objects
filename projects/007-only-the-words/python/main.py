import string


def get_string(words):
    list_of_words = ""

    for word in words:

        for character in word:

            if character in string.ascii_letters or character == "'" or character == "’" or character == " ":
                list_of_words += character

    return list_of_words.split()


def main():
    user_string = input("Enter a string: ")

    print(get_string(user_string))


if __name__ == '__main__':
    main()
