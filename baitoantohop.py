[n,k] = [int(x) for x in input().split()]
a = list(set( int(x) for x in input().split()))
a.sort()
a.insert(0,0)
n = len(a)-1
X = [0]*(n+5)
ans = [0]*(n+5)
def toHop(i,n,k):
    for j in range(X[i-1]+1,n-k+i+1):
        X[i] =j
        ans[i] = a[X[i]]
        if i==k:
            for m in range(1,k+1):
                print(ans[m],end= ' ')
            print()
        else:
            toHop(i+1,n,k)
            
toHop(1,n,k)
     
# 8 3
# 2 4 4 3 5 1 3 4