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
            return True
    
    #Checking for a crossed out row
    for i in range(5):
        row=[]
        for j in 'BINGO':
            row.append(CrossedCard[j][i])
        if sum(row)==0:
            return True
    
    #Checking for a crossed out diagonal
    diagonal=[]
    for i,j in zip('BINGO',range(5)):
        diagonal.append(CrossedCard[i][j])
    if sum(diagonal)==0:
        return True
    
    diagonal=[]
    for i,j in zip('BINGO',range(4,-1,-1)):
        diagonal.append(CrossedCard[i][j])
    if sum(diagonal)==0:
        return True
    
    return False

def BingoSession():
    numbers=list(range(1,76))
    extractions=[]
    card=BingoCard()
    number=choice(numbers)
    extractions.append(number)
    numbers.remove(number)
    crossedCard=CrossingOut(number,card)
    win_flag=False
    while len(numbers)>0 and not win_flag:
        number=choice(numbers)
        extractions.append(number)
        numbers.remove(number)
        crossedCard=CrossingOut(number,crossedCard)
        win_flag=CheckForWin(crossedCard)
    return len(extractions)

def main():
    calls=[]
    while len(calls)<1000:
        calls.append(BingoSession())
    max_calls=max(calls)
    min_calls=min(calls)
    mean_calls=int(sum(calls)/len(calls))
    print('Max calls: {}\nMin calls: {}\nMean calls: {}'.format(max_calls,min_calls,mean_calls))

if __name__=='__main__':
    main()