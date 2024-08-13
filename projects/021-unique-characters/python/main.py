'''
Create a program that determines and displays the number of unique characters in a string entered by the user. 

For example, *Hello, World!* has 10 unique characters while zzz has only one unique character. 

Use a dictionary or set to solve this problem.
'''

array = {
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
}

counter = 0

phrase = input("Please write a phrase: ").lower()
for char in phrase:
    if char in array:
        array.remove(char)
        counter += 1
       
print("Unique characters inside phrase: ", counter)
