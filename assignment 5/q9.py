a=[]
while True:  
    n=input('enter word: ')
    print("press q to stop")
    a.append(n)
    if(n=='q'):
        break
for i in a:
    j=a.count(i)
    print(i,':-',j)