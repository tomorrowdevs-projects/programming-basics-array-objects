def min_max_remover(list_value, integer_value):
    list_value_copy = list_value.copy()
    list_value_copy.sort()                       
    counter = 1

    while counter <= integer_value:
        list_value_copy.remove(max(list_value_copy))
        list_value_copy.remove(min(list_value_copy))
        counter += 1
    
    return list_value_copy
    
list_elements = []

user_input = float((input('insert value (insert 0 to stop): ')))
while user_input != 0:
    list_elements.append(user_input)
    user_input = float((input('insert value (insert 0 to stop): ')))

n = int(input('insert a non-negative integer: ')) 

if len(list_elements) < (n*2):
    print(f'number of values must be higher than {n*2}')

else:
    print(f'Copied list with elements removed: {min_max_remover(list_elements, n)}')
    print(f'Original list: {list_elements}')    


