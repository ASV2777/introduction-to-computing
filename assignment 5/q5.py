n=int(input('enter number of rows: '))
k=65
for i in range(1,n+1): 
    for j in range(1,i+1):
        print(chr(k),end=' ')
        k=k+1
        if k>90:
            k=65
    print()
    