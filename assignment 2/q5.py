a=int(input('enter side a '))
b=int(input('enter side b '))
c=int(input('enter side c '))
while a<b+c and b<a+c and c<a+b:
    print('yes')
    break
while a>b+c or b>a+c or c>a+b:
    print('no')
    break