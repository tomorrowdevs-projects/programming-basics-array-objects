def pressNumber(character):
    keyboard={1:'.,?!:',2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ',0:' '}
    for key in keyboard:
        group=keyboard.get(key)
        if character.upper() in group:
            i=group.index(character.upper())
            press=str(key)*(i+1)
            return press

def nokia3310(message):
    message_instructions=''
    for character in message:
        message_instructions=message_instructions+pressNumber(character)
    return message_instructions

def main():
    message=input('Please, enter the message that you want to send:')
    print(nokia3310(message))

if __name__=='__main__':
    main()
