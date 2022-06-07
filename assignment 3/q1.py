n=int(input('enter number '))
s=''
while n>=1:
    m=str(n%2)
    s=m+s
    n=n//2
print(s)