def morse(character):
    keyboard={
    'A': '._',
    'B': '_...',
    'C': '_._.',
    'D': '_..',
    'E': '.',
    'F': '.._.',
    'G': '__.',
    'H': '....',
    'I': '..',
    'J': '.___',
    'K': '_._',
    'L': '._..',
    'M': '__',
    'N': '_.',
    'O': '___',
    'P': '.__.',
    'Q': '__._',
    'R': '._.',
    'S': '...',
    'T': '_',
    'U': '.._',
    'V': '..._',
    'W': '.__',
    'X': '_.._',
    'Y': '_.__',
    'Z': '__..',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '0': '_____',
    'Á': '._._.',
    'Ä': '._._',
    'É': '.._..',
    'Ñ': '__.__',
    'Ö': '___ .',
    'Ü': '..__'}
    if character.upper() in keyboard:
        morse_char=keyboard[character.upper()]+' '
    else:
        morse_char=''
    return morse_char 

def morse_coder(message):
    message_instructions=''
    for character in message:
        message_instructions=message_instructions+morse(character)
    return message_instructions.rstrip(' ')

def main():
    message=input('Please, enter the message that you want to send:')
    print(morse_coder(message))

if __name__=='__main__':
    main()