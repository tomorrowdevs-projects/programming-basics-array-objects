def hist(string):
    word_dict = dict()
    for char in string:
        if char in word_dict:
            word_dict[char] += 1
        
        else:
            word_dict[char] = 1
    
    return word_dict


user_string_1 = input('insert first word: ').lower()
user_string_2 = input('insert second word: ').lower()

if hist(user_string_1) == hist(user_string_2):
    print(f'{user_string_1} and {user_string_2} are anagrams.')

else:
    print(f'{user_string_1} and {user_string_2} are not anagrams.')
