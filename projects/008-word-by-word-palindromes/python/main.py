import string


def get_string(words):
    list_of_words = ""
    character = 0

    while len(words) > character:

        if words[character] not in string.punctuation:
            list_of_words += words[character]

        elif character + 1 < len(words) and words[character + 1] == "'" and words[character + 1] == "’":
            list_of_words += words[character]

        character += 1

    return list_of_words.split()


def get_palindromes(user_string):
    is_palindrome = get_string(user_string)
    result = 0

    word_counter = 0

    for word in range(len(is_palindrome) // 2):

        if is_palindrome[word_counter].lower() == is_palindrome[-(word_counter + 1)].lower():
            result = "It's word by word palindrome!"
        else:
            result = "It isn't word by word palindrome!"
        word_counter += 1

    return result


def main():
    user_string = input("Enter a string: ")

    print(get_palindromes(user_string))


if __name__ == '__main__':
    main()