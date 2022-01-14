t = int(input())
while t>0 : 
    s= input()
    for i in range(0,len(s),2) : 
        b = s[i]
        n = int(s[i+1])        
        b = b*n
        print(b,end='')
    print()
    t-=1
