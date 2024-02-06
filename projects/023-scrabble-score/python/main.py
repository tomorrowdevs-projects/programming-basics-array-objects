def scrabble_score(message):
    letters = {
        1: ["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: "K",
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    total = 0
    for key, value in letters.items():

        for letter in message.upper():

            if letter in value:
                total += key

    return total


def main():
    user_message = input("Enter your message here: ")

    print(f"total point: {scrabble_score(user_message)}")


if __name__ == '__main__':
    main()
