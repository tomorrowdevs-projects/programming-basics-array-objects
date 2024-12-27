def hist(string_1, string_2 ):

    if len(string_1) != len(string_2):
        return False
    
    word_dict_1 = list()
    word_dict_2 = list()  
    
    for i in range(len(string_1)):
        word_dict_1.append(string_1[i])
        word_dict_2.append(string_2[i])
       
    word_dict_1.sort()
    word_dict_2.sort()

    return word_dict_1 == word_dict_2

user_string_1 = input('insert first word: ').lower()
user_string_2 = input('insert second word: ').lower()

is_anagram = hist(user_string_1, user_string_2)

if is_anagram:
    print(f'{user_string_1} and {user_string_2} are anagrams.')

else:
    print(f'{user_string_1} and {user_string_2} are not anagrams.')
