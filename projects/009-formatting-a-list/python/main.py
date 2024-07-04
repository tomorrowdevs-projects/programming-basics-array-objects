'''When writing out a list of items in English, one normally separates the items with commas. In addition, the word “and” is normally included before the last item, unless the list only contains one item. 

Consider the following four lists:
*apples*
*apples and oranges*
*apples, oranges and bananas*
*apples, oranges, bananas and lemons*

Write a function that takes a list of strings as its only parameter. Your function should return a string that contains all of the items in the list, formatted in the manner described previously, as its only result.
While the examples shown previously only include lists containing four elements or less, your function should behave correctly for lists of any length.
Include a main program that reads several items from the user, formats them by calling your function, and then displays the result returned by the function.'''

array = []
punctuation = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
risultato = ""
counter = 0

def function():
    global counter
    while True:
        parole = str(input("Please input a series of words: "))
        global array
        if parole == "":
            break
        else:
            array.append(parole)
            counter += 1

function()

for item in array:
    clean_item = ""
    for character in item:
        if character not in punctuation:
            clean_item += character
    risultato += clean_item
    counter -= 1
    if counter > 1:
        risultato += ", "
    elif counter == 1:
        risultato += " and "

print(risultato)