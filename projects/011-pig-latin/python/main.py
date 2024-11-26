user_input = input('Insert a string (only letters and spaces): ').lower()

string_list = user_input.split()
pig_latin_list = []
first_vowel_list = []
vowel_list = ['a', 'e', 'i', 'o', 'u']
counter = 0

for word in string_list:
    if word[0] in vowel_list:
        pig_latin_list.append(word + 'way')
        counter += 1
    
    else:
        for vowel in vowel_list:
            find_vowel = word.find(vowel)
            if find_vowel > 0:
                first_vowel_list.append(find_vowel) 
        
        first_vowel_list.sort()        
        slice_position = first_vowel_list[0]
        sliced_string = word[:slice_position]
        pig_latin_list.append(word[slice_position:] + sliced_string + 'ay')
        counter += 1

print(' '.join(pig_latin_list))