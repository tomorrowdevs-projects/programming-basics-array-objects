def anagrams(str_A, str_B):
    if sorted(str_A) == sorted(str_B):
        return True
    else:
        return False


def main():
    first_string = input("Enter the first string here: ")
    second_string = input("Enter the second string here: ")

    if anagrams(first_string, second_string):
        print(f"{first_string} and {second_string} are anagrams of each others!")

    else:
        print(f"{first_string} and {second_string} are not anagrams!")


if __name__ == '__main__':
    main()
