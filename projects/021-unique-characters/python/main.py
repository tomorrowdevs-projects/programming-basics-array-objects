def unique_characters(message):
    set_message = set(message)
    return set_message


def main():
    user_message = unique_characters(input("Enter your message here: "))

    print(f"There are {len(user_message)} items: {user_message}")


if __name__ == '__main__':
    main()
