import string


def pig_latin(user_input):
    list_user = ""

    for letter in user_input:

        if letter in string.ascii_letters or letter == " " or letter == "'":
            list_user += letter

    new_line = ""

    for word in list_user.lower().split():

        if word[0] in ("a", "e", "i", "o", "u"):
            new_line += word + "way"

        else:
            letter_counter = 0
            for letter in word:

                if letter in ("a", "e", "i", "o", "u"):
                    break

                letter_counter += 1

            new_line += word[letter_counter: len(word) + 1] + word[0:letter_counter] + "ay"

    return new_line


def main():
    user_input = input("Enter a line of text:\n")
    new_text = []

    for word in user_input.split():
        new_text.append(pig_latin(word))

    print(" ".join(new_text))


if __name__ == '__main__':
    main()
