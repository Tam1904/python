import math
N = int(input())
a = [int(x) for x in input().split()]
ans,sum,res=100000000,0,0
for i in range(N) :
    sum=0
    for j in range(N):
        if i!=j:
            sum+=int(math.fabs(a[i]-a[j]))
    if sum < ans :
        ans = sum
        res = a[i]
print(ans,res,sep=' ')

# 8
# 13 5 8 7 9 13 26 34