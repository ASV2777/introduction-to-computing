a=float(input('enter 1st side: '))
b=float(input('enter 2nd side: '))
c=float(input('enter 3rd side: '))
s=(a+b+c)/2
ar=s*(s-a)*(s-b)*(s-c)
if ar>0:
    print('area of triangle is: %0.2f'%(ar**0.5))
else:
    print('combination of sides not possible')