import string


def get_string(words):
    list_of_words = ""
    character = 0

    while len(words) > character:

        if words[character] not in string.punctuation:
            list_of_words += words[character]

        elif character + 1 < len(words) and words[character + 1] != "":
            list_of_words += words[character]

        character += 1

    return list_of_words.split()


def main():
    user_string = input("Enter a string: ")

    print(get_string(user_string))


if __name__ == '__main__':
    main()
