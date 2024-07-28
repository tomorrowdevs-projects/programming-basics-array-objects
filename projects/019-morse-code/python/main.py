'''
Morse code is an encoding scheme that uses dashes and dots to represent digits and letters. 
In this exercise, you will write a program that uses a dictionary to store the mapping from these symbols to Morse code. 

Use a period to represent a dot, and a hyphen to represent a dash. The mapping from characters to dashes and dots is shown in Table 6.1.

Your program should read a message from the user. Then it should translate all of
the letters and digits in the message to Morse code, leaving a space between each sequence of dashes and dots. 
Your program should ignore any characters that are not listed in the previous table. 

The Morse code for Hello, World! is shown below:


.... . .-.. .-.. --- .-- --- .-. .-.. -..

|Characted|Code|Character|Code|
|---------|----|---------|----|
|A|	. _|N|	_ .	| 
|B|	_ . . .|O|	_ _ _|	 
|C|_ . _ .|P|. _ _ .| 
|D|_ . .|Q|_ _ . _| 
|E|.|R|. _ .| 
|F|. . _ .|S|. . .| 
|G|_ _ .|T|_| 
|H|. . . .|U|. . _| 
|I|. .|V|. . . _| 
|J|. _ _ _|W|. _ _| 
|K|_ . _|X|_ . . _| 
|L|. _ . .|Y|_ . _ _| 
|M|_ _|Z|_ _ . .| 
 	 	 	 			 
Numbers

|Characted|Code|Character|Code|
|---------|----|---------|----|
|1|. _ _ _ _|6|_ . . . .| 
|2|. . _ _ _|7|_ _ . . .| 
|3|. . . _ _|8|_ _ _ . .| 
|4|. . . . _|9|_ _ _ _ .| 
|5|. . . . .|0|_ _ _ _ _| 
 	 	 	 			 
Acented characters

|Characted|Code|Character|Code|
|---------|----|---------|----|
|Á|. _ _ . _|Ä|. _ . _| 
|É|. . _ . .|Ñ|_ _ . _ _| 
|Ö|_ _ _ .|Ü|. . _ _|
'''

key_dictionary = {
    'A': '._', 'B': '_...', 'C': '_._.',
    'D': '_..', 'E': '.', 'F': '.._.',
    'G': '__.', 'H': '....', 'I': '..',
    'J': '.___', 'K': '_._', 'L': '._..',
    'M': '__', 'N': '_.', 'O': '___',
    'P': '.__.', 'Q': '__._', 'R': '._.', 'S': '...',
    'T': '_', 'U': '.._', 'V': '..._',
    'W': '.__', 'X': '_.._', 'Y': '_.__', 'Z': '__..',
    '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....', '6': '_....', '7': '__...', '8': '___..', '9': '____.', '0': '_____',
    'Á': '.__._', 'É': '.._..', 'Ö': '___.', 'Ä': '._._', 'Ñ': '__.__', 'Ü': '..__'
}

usermessage = input("Please input a message to convert to keypad presses: ")
convertedmessage = ""

for char in usermessage.upper():
    if char in key_dictionary:
        convertedmessage += key_dictionary[char]
        convertedmessage += ' '

print(convertedmessage)