def is_sublist(larger, smaller):
    new_list = []
    sublist = False

    for item in larger:

        if item in smaller:
            new_list.append(item)

        else:
            new_list = []

        if new_list == smaller:
            sublist = True
            break

        else:
            sublist = False

    return sublist


def main():
    main_list = [1, 2, 3, 4]

    assert is_sublist(main_list, [4, 5]) == False, "Should be False"
    assert is_sublist(main_list, []) == True, "Should be True!"
    assert is_sublist(main_list, [1, 3]) == False, "Should be False"
    assert is_sublist(main_list, [2, 3]) == True, "Should be True!"
    assert is_sublist(main_list, [1, 2, 3, 4]), "Should be True!"


if __name__ == '__main__':
    main()
