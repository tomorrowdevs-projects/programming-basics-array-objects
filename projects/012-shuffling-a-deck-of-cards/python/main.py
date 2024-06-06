from random import randint

def createDeck():
	suits=['s','h','d','c']
	figures=['T','J','Q','K']
	deck=list()
	for suit in suits:
		for value in range(1,14):
			if 1<value<10:
				deck.append('{}{}'.format(suit,value))
			elif value==1:
				deck.append('{}{}'.format(suit,'A'))
			else:
				index=value-10
				deck.append('{}{}'.format(suit,figures[index]))
	return deck

def shuffle_deck(deck):
	shuffled_deck=list()
	while len(shuffled_deck)<len(deck):
		shuffled_deck.append(0)
	for card in deck:
		index=randint(0,len(deck)-1)
		while shuffled_deck[index]!=0:
			index=randint(0,len(deck)-1)
		shuffled_deck[index]=card
	return shuffled_deck
	
def main():
	deck=createDeck()
	shuffled_deck=shuffle_deck(deck)
	print(deck)
	print(shuffled_deck)

if __name__=='__main__':
	main()