'''
On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are needed for most letters.
Pressing the number once generates the first character listed for that key.
Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth character.

|Key| Symbols|
|------|-----------|
|1| .,?!:|
|2| ABC|
|3| DEF|
|4 |GHI|
|5 |JKL|
|6| MNO|
|7| PQRS|
|8| TUV|
|9| WXYZ|
|0| space|

Write a program that displays the key presses needed for a message entered by the user.
Construct a dictionary that maps from each letter or symbol to the key presses needed to generate it.
Then use the dictionary to create and display the presses needed for the user’s message.
For example, if the user enters Hello, World! then your program should output 4433555555666110966677755531111.
Ensure that your program handles both uppercase and lowercase letters.
Ignore any characters that aren’t listed in the table above such as semicolons and parentheses.
'''

key_dictionary = {
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0'
}

usermessage = input("Please input a message to convert to keypad presses: ")
convertedmessage = ""

for char in usermessage.upper():
    if char in key_dictionary:
        convertedmessage += key_dictionary[char]

print(convertedmessage)