m=int(input('enter starting number: '))
n=int(input('enter ending number: '))
o=int(input('enter number whose muliples have to be printed: '))
for i in range(m,n+1):
    if i%o==0:
        print(i)