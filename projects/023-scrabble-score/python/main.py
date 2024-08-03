def scarabeo(word):
    LetterToPoints = {
        'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    points=0
    for letter in word:
        letter=letter.upper()
        if letter in LetterToPoints:
            points+=LetterToPoints[letter]
    return points

def main():
    word=input('Please, input a word:')
    print(scarabeo(word))

if __name__=='__main__':
    main()