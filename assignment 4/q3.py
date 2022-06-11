import random
i=1
while i<=10:
    r1=random.randint(1,10)
    r2=random.randint(1,10)
    print('Question',i,':',r1,'x',r2,'=',end='')
    n=int(input())
    if(n==r1*r2):
        print('Right!')
    else:
        print('Wrong.The answer is',r1*r2)
    print()
    i+=1