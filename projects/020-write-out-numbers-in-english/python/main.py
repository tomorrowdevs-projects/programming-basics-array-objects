'''
While the popularity of cheques as a payment method has diminished in recent years, some companies still issue them to pay employees or vendors.
The amount being paid normally appears on a cheque twice, with one occurrence written using digits, and the other occurrence written using English words. 

Repeating the amount in two different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.
In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that number. 

For example, if the parameter to the function is 142 then your function should return “one hundred forty two”. 

Use one or more dictionaries to implement your solution rather than large if/elif/else constructs. Include a main program that reads an integer from the user and displays its value in English words.
'''

unita = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
}

decine = {
    10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}

centinaia = {
    100: "one hundred", 200: "two hundred", 300: "three hundred", 400: "four hundred", 500: "five hundred",
    600: "six hundred", 700: "seven hundred", 800: "eight hundred", 900: "nine hundred"
}

def number_to_words(number):
    if number < 10:
        return unita[number]
    elif number < 100:
        decineinserite = (number // 10) * 10
        unitainserite = number % 10
        if unitainserite == 0:
            return decine[decineinserite]
        else:
            return decine[decineinserite] + ' ' + unita[unitainserite]
    elif number < 1000:
        centinaiainserite = (number // 100) * 100
        resto = number % 100
        if resto == 0:
            return centinaia[centinaiainserite]
        else:
            return centinaia[centinaiainserite] + ' ' + number_to_words(resto)

def main():
    numeroinserito = int(input("Please enter a number between 0 and 999: "))
    print(number_to_words(numeroinserito))

main()