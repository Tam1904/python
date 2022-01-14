import math
[n, m] = [int(x) for x in input().split()]
max = 100000
F = [True for i in range(0, max)]
for i in range(2, (int)(math.sqrt(max))):
    if F[i] == True:
        for j in range(i*i, max, i):
            F[j] = False
a = [0]
for i in range(2, max):
    if F[i] == True:
        a.append(int(i))
sum = m
for i in a :
    print(i+sum,end=' ')
    sum = i+ sum
    n-=1
    if n <0 : 
        break
