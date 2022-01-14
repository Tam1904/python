import math
n = int(input())
a = [int(x) for x in input().split()]
a.sort()
for i in range(n-1) :
    for j in range(i+1,n) : 
        if((int)(math.gcd(a[i],a[j]))==1) : 
            print(a[i],a[j],sep=' ')
# 5
# 3 7 9 6 13