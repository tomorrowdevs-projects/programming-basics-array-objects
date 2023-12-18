import string


def morse_code(message):
    # Upper
    letters = string.ascii_uppercase
    letters_code = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__", "_.",
                    "___",
                    ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__.."]
    letters_dict = {letter: code for letter, code in zip(letters, letters_code)}

    # Numbers
    numbers_dict = {
        "1": ".____",
        "2": "..___",
        "3": "...__",
        "4": "...._",
        "5": ".....",
        "6": "_....",
        "7": "__...",
        "8": "___..",
        "9": "____.",
        "0": "_____"
    }

    # Accented characters
    accented_characters = {
        "Á": ".__._",
        "Ä": "._._",
        "É": ".._..",
        "Ñ": "__.__",
        "Ö": "___.",
        "Ü": "..__"
    }

    code = ""
    for character in message.upper():

        if character in letters_dict:
            code += letters_dict[character] + " "
        if character in numbers_dict:
            code += numbers_dict[character] + " "
        if character in accented_characters:
            code += accented_characters[character] + " "

    return code


def main():
    user_message = input("Enter your message here: ")

    print(morse_code(user_message))


if __name__ == '__main__':
    main()
