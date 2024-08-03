from random import choices

def BingoCard():
    card={}
    card['B']=choices(range(1,16),k=5)
    card['I']=choices(range(16,31),k=5)
    card['N']=choices(range(31,46),k=5)
    card['G']=choices(range(46,61),k=5)
    card['O']=choices(range(61,76),k=5)
    return card

def main():
    card=BingoCard()
    print(' B   I   N   G   O')
    print('-'*len(' B   I   N   G   O'))
    for i in range(5):
        row=''
        row='{:2d}'.format(card['B'][i])
        for j in 'INGO':
            row=row+'{:4d}'.format(card[j][i])
        print(row)

if __name__=='__main__':
    main()