import math
N = int(input())
a = [int(x) for x in input().split()]
F = [0]*10005
F[0] = F[1] = 1
for i in range(2, int(math.sqrt(10005)+1)):
    if F[i] == 0:
        for j in range(i*i, 10005, i):
            F[j] = 1
P = []
for i in range(2, 10001):
    if F[i] == 0:
        P.append(i)
ans,sum =0,0
for i in a:
    if F[i] != 0:
        if i<P[0] :
            sum = P[0]-i
        elif i >P[len(P)-1] :
            sum = i -P[len(P)-1]
        else : 
             for j in range(len(P)-1):
                if P[j] < i < P[j+1]:
                    sum=min(i-P[j],P[j+1]-i)
        ans = max(ans,sum)
print(ans)
# 9
# 13 0 5 8 7 9 15 26 34