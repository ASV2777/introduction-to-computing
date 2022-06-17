a=[]
for i in range(10):
    n=int(input("enter a number: "))
    a.append(n)
print("positive numbers : ",end='') 
for j in a:
    if j>=0:
        print(j,end=' ')
print()
print('negative numbers : ',end='')
for j in a:
    if j<0:
        print(j,end=' ')
print()
print('odd numbers : ',end='')
for j in a:
    if j%2!=0:
        print(j,end=' ')
print()
print('even numbers : ',end='')
for j in a:
    if j%2==0:
        print(j,end=' ')
print()
for j in a:
    k=a.count(j)
    print(j,':-',k)