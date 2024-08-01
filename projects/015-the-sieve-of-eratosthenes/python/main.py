def primeNumbers(limit):
    numbers=list(range(limit+1))
    numbers[1]=0
    prime_numbers=[]
    for number in numbers:
        if number>0:
            prime_numbers.append(number)
            index=range(number*2,limit+1,number)
            for i in index:
                numbers[i]=0
    return prime_numbers

def main():
    limit=int(input('Please, enter the limit number for the prime numbers research:'))
    prime_numbers=primeNumbers(limit)
    print(prime_numbers)

if __name__=='__main__':
    main()