import math
[n,m] = [int(x) for x in input().split()]
A = []
index = 1005
F = [True for i in range(index)]
F = [False,False] + F
for i in range(2,(int)(math.sqrt(index))) : 
    if F[i] == True : 
        for j in range(i*i,index,i) :
            F[j] = False

for i in range(n) :
    b =[ 1 if F[(int(x))] else 0 for x in input().split()]
    A.append(b)
for i in range(n) : 
    for j in range(m) : 
        print(A[i][j],end=' ')
    print()
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9