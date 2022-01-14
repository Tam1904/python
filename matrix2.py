import math
N = int(input())
A = [[int(x) for x in input().split()] for i in range(0,N)]
K = int(input())
sum1,sum2=0,0
for i in range(0,N):
    for j in range(0,N):
        if i + j > N :
            sum1+=A[i][j]
        if i + j < N-1:
            sum2+=A[i][j]
sum = int(math.fabs(sum1-sum2))
if sum<=K:
    print("YES")
else:
    print("NO")

print(sum)
# 5
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9
# 5