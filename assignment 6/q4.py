def pangram(a):
    c=0
    a=a.upper()
    for i in range(65,91):
        if chr(i) in a:
            c+=1
    if c>=26:
        print('pangram')
    else:
        print('not pangram')
pangram('the quick brown fox jumps over the lazy dog')