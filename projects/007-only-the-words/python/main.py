'''
In this exercise you will create a program that identifies all of the words in a string entered by the user. Begin by writing a function that takes a string as its only parameter. 
Your function should return a list of the words in the string with the punctuation marks at the edges of the words removed. 
The punctu-ation marks that you must consider include commas, periods, question marks, hyphens, apostrophes, exclamation points, colons, and semicolons. 
Do not remove punctuation marks that appear in the middle of a word, such as the apostrophes used to form a contraction. 
For example, if your function is provided with the string *"Contractions include: don’t, isn’t, and wouldn’t."* then your function should return the list *["Contractions", "include", "don’t", "isn’t", "and", "wouldn’t"]*.
Write a main program that demonstrates your function. 
It should read a string from the user and then display all of the words in the string with the punctuation marks removed.
'''

array = []
punctuation = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
risultato = ""

def function():
    while True:
        m = str(input("Please input a string: "))
        global array
        if m == "":
            break
        else:
            array.append(m)

function()

for item in array:
    if len(item) > 0:
        risultato += item[0]
        for character in item[1:-1]:
            if character not in punctuation:
                risultato += character
        if len(item) > 1 and item[-1] in punctuation:
            risultato += item[-1]
        risultato += " "

print(risultato)