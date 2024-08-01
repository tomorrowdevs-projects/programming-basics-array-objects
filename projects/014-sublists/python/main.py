def isSublist(mainList,subList):
    for i in range(len(mainList)):
        mainList[i]=str(mainList[i])
    mainList=''.join(mainList)

    for i in range(len(subList)):
        subList[i]=str(subList[i])
    subList=''.join(subList)

    return subList in mainList

def main():
    element='0'
    mainList=[]
    while element!='':
        element=input('Enter a main list (void input to end the list):')
        if element!='':
            mainList.append(element)
    
    element='0'
    subList=[]
    while element!='':
        element=input('Enter the list to be checked (void input to end the list):')
        if element!='':
            subList.append(element)
    
    if isSublist(mainList,subList):
        print('{} is a sublist of {}'.format(subList,mainList))
    else:
        print('{} is not a sublist of {}'.format(subList,mainList))

if __name__=='__main__':
    main()