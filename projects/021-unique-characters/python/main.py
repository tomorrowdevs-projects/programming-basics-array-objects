unique_char = set()

user_input = input('Insert a string: ')

for char in user_input:
    unique_char.add(char)

print(f'"{user_input}" has {len(unique_char)} unique characters.')
