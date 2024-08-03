from random import choice,sample
from copy import deepcopy

def BingoCard():
    card={}
    card['B']=sample(range(1,16),k=5)
    card['I']=sample(range(16,31),k=5)
    card['N']=sample(range(31,46),k=5)
    card['G']=sample(range(46,61),k=5)
    card['O']=sample(range(61,76),k=5)
    return card

def PrintCard(card):
    print(' B   I   N   G   O')
    print('-'*len(' B   I   N   G   O'))
    for i in range(5):
        row=''
        row='{:2d}'.format(card['B'][i])
        for j in 'INGO':
            row=row+'{:4d}'.format(card[j][i])
        print(row)

def CrossingOut(number,card):
    crossedCard=deepcopy(card)
    for i,j in zip(card.keys(),card.values()):
        if number in j:
            crossedCard[i][j.index(number)]=0
    return crossedCard

def CheckForWin(CrossedCard):
    #Checking for a crossed out column
    for i in CrossedCard.values():
        if sum(i)==0:
            return 'column'
    
    #Checking for a crossed out row
    for i in range(5):
        row=[]
        for j in 'BINGO':
            row.append(CrossedCard[j][i])
        if sum(row)==0:
            return 'row'
    
    #Checking for a crossed out diagonal
    diagonal=[]
    for i,j in zip('BINGO',range(5)):
        diagonal.append(CrossedCard[i][j])
    if sum(diagonal)==0:
        return 'diagonal'
    
    diagonal=[]
    for i,j in zip('BINGO',range(4,-1,-1)):
        diagonal.append(CrossedCard[i][j])
    if sum(diagonal)==0:
        return 'diagonal'
    
    return 'nothing'

def BingoSession():
    numbers=list(range(1,76))
    extractions=[]
    card=BingoCard()
    number=choice(numbers)
    extractions.append(number)
    numbers.remove(number)
    crossedCard=CrossingOut(number,card)
    type_win='nothing'
    while len(numbers)>0 and type_win=='nothing':
        number=choice(numbers)
        extractions.append(number)
        numbers.remove(number)
        crossedCard=CrossingOut(number,crossedCard)
        type_win=CheckForWin(crossedCard)
    return [card,crossedCard,extractions,type_win]

def main():
    case_dic={'column':0,'row':0,'diagonal':0}
    card_dic=dict()
    extractions_dic=dict()
    crossed_card_dic=dict()
    while 0 in set(case_dic.values()):
        [card,crossedCard,extractions,type_win]=BingoSession()
        if case_dic[type_win]==0 and type_win!='nothing':
            card_dic[type_win]=card
            extractions_dic[type_win]=extractions
            crossed_card_dic[type_win]=crossedCard
        case_dic[type_win]+=1
    for i in case_dic:
        print('-'*25)
        print('{} CEHCKED OUT'.format(i.upper()))
        print('Extractions: {}\n'.format(extractions_dic[i]))
        PrintCard(card_dic[i])
        print('\n')
        PrintCard(crossed_card_dic[i])
        print('-'*25)

if __name__=='__main__':
    main()