from random import choice

def lottery_extraction():
	extraction=list()
	numbers=range(1,50)
	while len(extraction)<=6:
		number=choice(numbers)
		if not number in extraction:
			extraction.append(number)
	return extraction

def main():
		extraction=lottery_extraction()
		extraction.sort()
		print(extraction)

if __name__=='__main__':
	main()	