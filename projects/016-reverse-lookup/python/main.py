def reverseLookup(LookupDict,value):
    keyList=[]
    for key in LookupDict:
        if LookupDict.get(key,0)==value:
            keyList.append(key)
    return keyList

def main():
    dict1={'a':1,'b':2,'c':3}
    dict2={'a':1,'b':1,'c':3}
    dict3={'a':0,'b':2,'c':4}
    keyList1=reverseLookup(dict1,1)
    keyList2=reverseLookup(dict2,1)
    keyList3=reverseLookup(dict3,1)
    print('Here some examples:\n- dictionary 1: {} --> result: {}\n- dictionary 2: {} --> result: {}\n- dictionary 2: {} --> result: {}'.format(dict1,keyList1,dict2,keyList2,dict3,keyList3))

if __name__=='__main__':
    main()