'''
An integer, *n*, is said to be perfect when the sum of all of the proper divisors of *n* is equal to *n*. 
For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether or not a positive integer is perfect. 
Your function will take one parameter. If that parameter is a perfect number then your function will return True. 
Otherwise it will return False. 
In addition, write a main program that uses your function to identify and display all of the perfect numbers between 1 and 10,000.
'''

m = int(input("Please insert an integer number: "))
array = []

def function():
    for n in range(1, m):
        if m % n == 0:
            array.append(n)

def sum_function():
    global sumarray
    global check
    sumarray = sum(array)
    if sumarray == m:
        check = True
    else:
        check = False

function()
sum_function()
if check:
    print("The number is perfect!")
else:
    print("The number is NOT perfect!")