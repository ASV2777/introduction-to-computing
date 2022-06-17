m= int(input ("Enter starting number: "))  
n= int(input ("Enter ending number: "))    
print ("The Prime Numbers in the range are: ")  
for i in range(m,n+1):
    count=0
    for j in range(1,i//2+1):
        if i%j==0:
            count+=1
    if(count==1):    
        print(i) 