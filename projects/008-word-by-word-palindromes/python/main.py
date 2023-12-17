import string


def get_string(words):
    list_of_words = ""

    for word in words:

        for character in word:

            if character in string.ascii_letters or character == "'" or character == "’" or character == " ":
                list_of_words += character

    return list_of_words


def get_palindromes(user_string):
    is_palindrome = get_string(user_string)
    result = "It isn't word by word palindrome!"

    word_counter = 0

    for word in range(len(is_palindrome) // 2):

        if is_palindrome[word_counter].lower() == is_palindrome[-(word_counter + 1)].lower():
            result = "It's word by word palindrome!"

        word_counter += 1

    return result


def main():
    user_string = input("Enter a string: ")

    print(get_palindromes(user_string))


if __name__ == '__main__':
    main()