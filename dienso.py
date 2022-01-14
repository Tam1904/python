t = int(input())
while t>0:
    n = int(input())
    a = [int(x) for x in input().split()]
    ans =0
    a.sort()
    for i in range(n-1):
        if a[i]+1< a[i+1]:
            ans+=a[i+1]-a[i]-1
    print(ans)
    t-=1
# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3