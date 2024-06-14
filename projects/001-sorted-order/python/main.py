#Write a program that reads integers from the user and stores them in an array. 
#Your program should continue reading values until the user enters 0. 
#Then it should display all of the values entered by the user (except for the 0) in ascending order, with one value appearing on each line. 
#Use either the sort method or the sorted function to sort the array.

array = []

while True:
    numbers = int(input("Please input a numbe (input 0 if you want to end the code): "))
    array.append(numbers)
    if numbers == 0:
        break

array = array[:-1]
array.sort()
print("The numbers inserted were: ", *array, sep = "\n")
