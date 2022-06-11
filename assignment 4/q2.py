n=int(input('enter the year: '))
if (n%100==0):
    if(n%400==0):     
        print('leap year')
    else:
        print('not leap year')
elif (n%4==0):
    print("leap year")
else:
    print("not leap year")