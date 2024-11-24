def formatting_list (item_list):
    items_number = len(item_list)

    if items_number <= 1:
        string_result = ''.join(item_list)
    
    elif items_number == 2:
        string_result = ' and '.join(item_list)
    
    else:
        first_slice = ', '.join(item_list[:items_number-1])
        second_slice = ''.join(item_list[items_number-1:])
        string_result = first_slice + ' and ' + second_slice
        
    return string_result

list_from_user = []

user_input = input('insert an item (leave blank to stop): ')
while user_input != '':
    list_from_user.append(user_input)
    user_input = input('insert an item (leave blank to stop): ')

print(formatting_list(list_from_user))

