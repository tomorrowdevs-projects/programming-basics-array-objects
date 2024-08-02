def NumToLetters(number):
    base_dic = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
        }

    if number in base_dic:
        return base_dic[number]
    else:
        number_str=''
        if number//100>0:
            number_str=number_str+'{} hundred'.format(base_dic[number//100])
        if number%100//10>=2:
            number_str=number_str+' '+base_dic[number%100//10*10]
        if number%100%10>0:
            number_str=number_str+' '+base_dic[number%100%10]
        return number_str

def main():
    number=int(input('Please, enter a number between 0 and 999 in digits:'))
    print("""Here's {} in letters: {}""".format(number,NumToLetters(number)))

if __name__=='__main__':
    main()