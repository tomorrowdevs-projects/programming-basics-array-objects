import string
counter = 0
is_palindrome = True

user_input = input('Insert a string: ')
user_input = user_input.casefold()

for punctuation in string.punctuation:
    user_input = user_input.replace(punctuation, '')

cleaned_list = user_input.split()
words_in_list = len(cleaned_list)-1

for word in cleaned_list:
    if word == cleaned_list[(words_in_list)-counter]:
        counter += 1
    else:
        is_palindrome = False
        break

if is_palindrome == True:
    print('The string is palindrome')

else:
    print('The string is not palindrome')
