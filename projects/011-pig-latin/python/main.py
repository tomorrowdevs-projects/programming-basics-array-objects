def pig_latin(text):
	text=text.split()
	vowels=['a','e','i','o','u']
	j=0
	for word in text:
		if word[0] in vowels:
			word=word+'way'
		else:
			i=0
			while not word[i] in vowels:
				i+=1
			word=word[i:]+word[:i]+'ay'
		text[j]=word
		j+=1
	text=' '.join(text)
	return text
	
def main():
	text=input('Enter a text (only lower case letters and spaces:')
	text=pig_latin(text)
	print(text)

if __name__=='__main__':
	main()