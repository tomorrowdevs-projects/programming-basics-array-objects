integers_list=[]

is_valid_input=False
while not(is_valid_input):
    try:
        integer=int(input("Enter an integer (0 to quit): "))
        is_valid_input=True
    except ValueError:
        print("Invalid integer!")

while integer!=0:
    integers_list.append(integer)

    is_valid_input=False
    while not(is_valid_input):
        try:
            integer=int(input("Enter an integer (0 to quit): "))
            is_valid_input=True
        except ValueError:
            print("Invalid integer!")

for integer in sorted(integers_list):
    print(integer)