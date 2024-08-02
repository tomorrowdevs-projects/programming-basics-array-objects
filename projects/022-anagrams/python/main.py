def anagrams(word1,word2):
    word1=word1.lower()
    word2=word2.lower()
    
    word1_set=set(word1)
    word2_set=set(word2)
    if word1_set!=word2_set:
        return False
    else:
        word1_dic={}
        for i in word1_set:
            word1_dic[i]=0
        for i in word1:
            word1_dic[i]+=1

        word2_dic={}
        for i in word2_set:
            word2_dic[i]=0
        for i in word2:
            word2_dic[i]+=1
        
        if sum(word1_dic.values())==sum(word2_dic.values()):
            return True
        else:
            return False

def main():
    word1=input('Please, enter the first word:')
    word2=input('Please, entere the second word:')
    if anagrams(word1,word2):
        print('{} and {} are anagrams'.format(word1,word2))
    else:
        print('{} and {} are not anagrams'.format(word1,word2))

if __name__=='__main__':
    main()