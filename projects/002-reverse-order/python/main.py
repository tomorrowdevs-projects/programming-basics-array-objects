#Write a program that reads integers from the user and stores them in an array. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order, with one value appearing on each line.

array = []

while True:
    numbers = int(input("Please input a number (input 0 if you want to end the code): "))
    array.append(numbers)
    if numbers == 0:
        break

array = array[:-1]
array.sort()
reverse_array = array[::-1]
print("The numbers inserted were: ", *reverse_array, sep = "\n")