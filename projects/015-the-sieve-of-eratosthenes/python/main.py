user_limit = int(input('Insert a limit: '))

list_num = list(range(2, user_limit - 1))
limit = list_num[-1]
p = 2

while p <= limit:
    if list_num[p-2] == 0:
        p += 1
    
    else:
        for n in range(limit):
            multi = p * n 
            
            if list_num.count(multi) != 0 and multi != p:
                position = list_num.index(multi)
                remove = list_num.pop(position)
                list_num.insert(position, 0)
        
        p += 1

print(list_num)
