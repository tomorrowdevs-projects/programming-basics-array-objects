'''
Two words are anagrams if they contain all of the same letters, but in a different order. 

For example, “evil” and “live” are anagrams because each contains one “e”, one “i”, one “l”, and one “v”. 

Create a program that reads two strings from the user,
determines whether or not they are anagrams, and reports the result.
'''

array1 = []
array2 = []

firstword = input("Please input a word: ").lower()
secondword = input("Please input an anagram of the first word: ").lower()

for char in firstword:
    array1.append(char)
   
for char in secondword:
    array2.append(char)
   
array1.sort()
array2.sort()

if array1 == array2:
    print("The two words are anagrams")
else:
    print("The two words are NOT anagrams")