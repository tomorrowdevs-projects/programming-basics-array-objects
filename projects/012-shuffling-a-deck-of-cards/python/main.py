import random

def createDeck():
    suite_list = ['s', 'c', 'd', 'h']
    character_list = ['T', 'J', 'Q', 'K', 'A']
    deck_list = []
    
    for suite in suite_list:
        number = 2
        while number <= 9:
            deck_list.append(str(number) + suite)
            number += 1
        
        for character in character_list:
            deck_list.append( character + suite)
    
    return deck_list

def shuffle(deck_to_shuffle):    
    for card in range(len(deck_to_shuffle)): 
        deck_to_shuffle.insert(random.choice(range(card, len(deck_to_shuffle)+1)), deck_to_shuffle[0])
        deck_to_shuffle.pop(0)

    return deck_to_shuffle


new_deck = createDeck()

print(f'New deck: {new_deck}\n')
print(f'Shuffled deck: {shuffle(new_deck)}')

