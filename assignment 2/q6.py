a=int(input('enter number a '))
b=int(input('enter number b '))
c=bin(a^b)
d=str(c)
e=(d.count('1'))
print('number of bits that need to be flipped are:',e)