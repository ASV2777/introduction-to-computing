def palin(a):
    b=a[::-1]
    if(a==b):
        print('pallindrome')
    else:
        print('not pallindrome')
a=input('enter a string: ')
palin(a)
