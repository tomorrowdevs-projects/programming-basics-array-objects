def isSublist(larger_list, smaller_list):
    is_sub = False
    for item in range(len(larger_list) - len(smaller_list) + 1):
        if larger_list[item : item + len(smaller_list)] == smaller_list:
            is_sub = True
            break
    return is_sub

list_1 = []
list_2 = []

user_larger = input('Insert a value for the list 1 (empty to stop): ')
while user_larger != '':
    list_1.append(user_larger)
    user_larger = input('Insert a value for the list 1 (empty to stop): ')

user_smaller = input('Insert a value for the list 2 (empty to stop): ')
while user_smaller != '':
    list_2.append(user_smaller)
    user_smaller = input('Insert a value for the list 2 (empty to stop): ')    

if isSublist(list_1, list_2):
    print ('list 2 is a sublist of list 1')

else:
    print ('list 2 is not a sublist of list 1')

