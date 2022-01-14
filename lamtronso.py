t = (int)(input())
while t>0 : 
    N = str(input())
    if(len(N)==1) : 
        print(N)
    else :
        a = []
        for i in N : 
            a.append(int(i))
        for i in range(len(N)-1,0,-1) : 
            if a[i]>=5 :
                a[i]=0
                a[i-1]+=1
            else :
                a[i]=0
        print("".join(map(str, a)))
    t-=1
