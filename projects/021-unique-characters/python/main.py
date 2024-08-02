from time import monotonic

def byset(text):
    unique_set=set(text)
    print("""Your text contains {} unique characters""".format(len(unique_set)))

def bydic(text):
    unique_set={}
    for character in text:
        unique_set[character]=1
    print("""Your text contains {} unique characters""".format(len(unique_set)))

def main():
    text=input('Input a text:')

    t0=monotonic()
    byset(text)
    t1=monotonic()
    dt_set=t1-t0

    t0=monotonic()
    bydic(text)
    t1=monotonic()
    dt_dic=t1-t0

    print('The operation with set takes {} s, and with dictionary takes {} s'.format(dt_set,dt_dic))


if __name__=='__main__':
    main()