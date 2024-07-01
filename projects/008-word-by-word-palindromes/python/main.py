'''
A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.

Such palindromes examined the characters in a string, possibly ignoring spacing and punctuation marks, to see if the string was the same forwards and backwards. 
While palindromes are most commonly considered character by character, the notion of a palindrome can be extended to larger units. 
For example, while the sentence *“Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?”* isn’t a character by character palindrome, it is a palindrome when examined a word at a time (and when capitalization and punctuation are ignored). Other examples of word by word palindromes include *“Herb the sage eats sage, the herb”*
and *“Information school graduate seeks graduate school information”*.

Create a program that reads a string from the user. 
Your program should report whether or not the entered string is a word by word palindrome. 
Ignore spacing and punctuation when determining the result.
'''

array = []
punctuation = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
risultato = ""
comparison_risultato = ""

def function():
    while True:
        palindrome = str(input("Please input a palindrome word or phrase: "))
        global array
        if palindrome == "":
            break
        else:
            array.append(palindrome)

function()

for item in array:
    for character in item:
        if character not in punctuation and character != " ":
            risultato += character.lower()
    risultato += " "

for item in reversed(array):
    for character in item:
        if character not in punctuation and character != " ":
            comparison_risultato += character.lower()
    comparison_risultato += " "

print("Input string without punctuation and spaces:", risultato.strip())
print("Reversed string without punctuation and spaces:", comparison_risultato.strip())

if risultato.strip() == comparison_risultato.strip():
    print("The input is a palindrome!")
else:
    print("The input is not a palindrome.")