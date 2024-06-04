def only_words(text):
	chars_to_delete=[",",".","?","!",":",";","-"]
	text=text.split()
	for i in range(len(text)):
		for char in chars_to_delete:
			word=text[i]
			word=word.lstrip(char)
			word=word.rstrip(char)
			text[i]=word
	return text

def main():
	text=input('Enter a text:')
	text=only_words(text)
	print(text)

if __name__=='__main__':
	main()