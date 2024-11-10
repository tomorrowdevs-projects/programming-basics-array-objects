
def divisors_function(n):
    list_divisors = []
    divisor = n
    while divisor > 0:
        if n % divisor == 0:
            list_divisors.append(divisor)
            divisor -= 1
        else:
            divisor -= 1
    return list_divisors

user_input = int(input('Insert an integer: '))

if user_input < 1:
    print('Integer must be > 0')

else:
    print(divisors_function(user_input))



        

