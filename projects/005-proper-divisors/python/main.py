'''
A proper divisor of a positive integer, *n*, is a positive integer less than *n* which divides evenly into *n*.
Write a function that computes all of the proper divisors of a positive integer. The integer will be passed to the function as its only parameter.
The function will return a list containing all of the proper divisors as its only result. Complete this exercise by writing a main program that demonstrates the function by reading a value from the user and displaying the list of its proper divisors.
Ensure that your main program only runs when your solution has not been imported into another file.
'''

m = int(input("Please insert an integer number: "))
array = []

def function():
    for n in range(1, m+1):
        if m % n == 0:
            array.append(n)

function()

print(array)