import string


def get_token(expression):
    tokens = []

    for token in expression.split():

        if len(token) > 1:
            numbers = ""

            for character in token:

                if character in string.digits:
                    numbers += character

                else:
                    if numbers != "":
                        tokens.append(numbers)
                        numbers = ""
                    tokens.append(character)

                if numbers != "":
                    tokens.append(numbers)
                    numbers = ""

        elif token != " ":
            tokens.append(token)

    return ", ".join(tokens)


def main():
    expression = input("Enter here your expression: ")

    print(get_token(expression))


if __name__ == '__main__':
    main()
