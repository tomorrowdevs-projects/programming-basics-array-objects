letters = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '.._.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
}

numbers = {
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
}

acented_characters = {
    'à' : '.--.-',
    'é' : '..-..',
    'ö' : '---.',
    'ä' : '.-.-',
    'ñ' : '--.--',
    'ü' : '..--'
}
    
output_list = [] 

user_input = input('Insert a text: ').lower()

for char in user_input:
    if char in letters:
        output_list.append(letters[char])
    
    elif char in numbers:
        output_list.append(numbers[char])
    
    elif char in acented_characters:
        output_list.append(acented_characters[char])
    
    else:
        continue

print(*output_list)
