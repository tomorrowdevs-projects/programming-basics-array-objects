def perfect_function(n):
    list_divisors = []
    divisor = n - 1
    while divisor > 0:
        if n % divisor == 0:
            list_divisors.append(divisor)
            divisor -= 1
        else:
            divisor -= 1
    
    if sum(list_divisors) == n:
        is_perfect = True
    
    else:
        is_perfect = False
    
    return is_perfect
    

for number in range(1, 10001):
    if perfect_function(number):
        print(number)