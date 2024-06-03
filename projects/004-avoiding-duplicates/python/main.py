def read_input():
    input_list=list()
    word=input('Enter a something:')
    while word!='':
        input_list.append(word)
        word=input('Enter a something:')
    return input_list

def delete_duplicate(input_list):
    singleton_list=list()
    for word in input_list:
        if word in singleton_list:
            pass
        else:
            singleton_list.append(word)
    return singleton_list

def main():
    input_list=read_input()
    singleton_list=delete_duplicate(input_list)
    print(singleton_list)

if __name__=='__main__':
    main()