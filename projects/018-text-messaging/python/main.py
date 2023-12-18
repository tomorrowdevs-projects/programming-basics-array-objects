def text_messaging(message):
    dictionary = {
        1: [".", ",", "?", "!", ":"],
        2: ["A", "B", "C"],
        3: ["D", "E", "F"],
        4: ["G", "H", "I"],
        5: ["J", "K", "L"],
        6: ["M", "N", "O"],
        7: ["P", "Q", "R", "S"],
        8: ["T", "U", "V"],
        9: ["W", "X", "Y", "Z"],
        0: [" "]
    }
    new_message = ""

    for letter in message.upper():

        for key, value in dictionary.items():

            if letter in value:
                index = value.index(letter)

                for n in range(index + 1):
                    new_message += str(key)

    return new_message


def main():
    user_message = input("Enter your message here: ")

    print(text_messaging(user_message))


if __name__ == '__main__':
    main()
