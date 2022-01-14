[a,K,N] = [int(x) for x in input().split()]
OK =0
l = (int)(a/K)
r = (int)(N/K)
if(l>=r) :
    print(-1)
else : 
    for i in range(l+1,r+1) : 
        print(K*i-a,end = ' ')
        