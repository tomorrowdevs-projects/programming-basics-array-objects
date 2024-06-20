'''
In this exercise, you will create a program that reads words from the user until the user enters a blank line. 
After the user enters a blank line your program should dis- play each word entered by the user exactly once. 
The words should be displayed in the same order that they were first entered. 

For example, if the user enters:
*first*
*second*
*first*
*third*
*second*

then your program should display:
*first*
*second*
*third*
'''

array = []

while True:
    n = str(input("Please input a word (leave blank to stop the input): "))
    if n == "":
        break
    else:
        array.append(n)
for item in set(array):
    if array.count(item) == 2:
        array.remove(item)
print("The numbers inserted were: ", *array, sep = "\n")