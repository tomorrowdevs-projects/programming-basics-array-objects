'''
Write a function named reverseLookup that finds all of the keys in a dictionary that map to a specific value. 
The function will take the dictionary and the value to search for as its only parameters. 
It will return a (possibly empty) list of keys from the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function as part of your solution to this exercise. 
Your program should create a dictionary and then show that the reverseLookup function works correctly when it returns multiple keys, a single key, and no keys. 
Ensure that your main program only runs when the file containing your solution to this exercise has not been imported into another program.
'''

def reverseLookup(dictionary, value):
    keys = []
    
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    
    return keys

def main():
    example_dict = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3,
        'e': 1
    }
    
    print("Keys with value 1:", reverseLookup(example_dict, 1))
    
    print("Keys with value 2:", reverseLookup(example_dict, 2))
    
    print("Keys with value 4:", reverseLookup(example_dict, 4))

main()