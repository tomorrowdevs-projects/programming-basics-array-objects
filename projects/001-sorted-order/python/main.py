integers_list=[]

integer=1

while integer!=0:
    try:        
        integer=int(input("Enter an integer (0 to quit): "))
        integers_list.append(integer)

    except ValueError:
        print("Invalid integer!")
        continue
integers_list.pop()
for integer in sorted(integers_list):
    print(integer)