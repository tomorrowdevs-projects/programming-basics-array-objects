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

def text_is_palindrome(text):
	text=only_words(text)
	palindrome_flag=True
	i=0
	while i<=len(text)//2 and palindrome_flag:
		palindrome_flag=text[i]==text[len(text)-i-1]
		i+=1
	return palindrome_flag

def main():
	text=input('Enter a text:')
	if text_is_palindrome(text):
		print('"{}" is palindrome'.format(text))
	else:
		print('"{}" is not palindrome'.format(text))

if __name__=='__main__':
	main()