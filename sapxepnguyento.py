import math
N = int(input())
a = [int(x) for x in input().split()]
F = [0]*1005
F[0] = F[1] = 1
for i in range(2, int(math.sqrt(1005)+1)):
    if F[i] == 0:
        for j in range(i*i, 1005, i):
            F[j] = 1
b = []
for i in a :
    if F[i]==0:
        b.append(i)
b.sort()
k=0
for i in range(N):
    if F[a[i]] == 1:
        print(a[i], end = ' ')
    else :
        print(b[k], end = ' ')
        k+=1