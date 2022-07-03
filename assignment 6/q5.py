def hypseq(a):
    if '-' not in a:
        print('invalid input')
    else:
        b=a.split('-')
        b.sort()
        k=1
        for i in b:
            if k==len(b):
                print(i)
            else:
                print(i,end='-')
            k+=1
hypseq('green-red-yellow-black-white')