def avoiding_duplicates():
    words = []

    while True:

        word = input("Enter a word or press enter to close:\n")

        if word == "":
            break

        if word not in words:
            words.append(word)

    return "; ".join(words)