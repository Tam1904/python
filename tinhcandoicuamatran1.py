import math

N = int(input())
a = []
for i in range(N):
    b = [int(x) for x in input().split()]
    a.append(b)
K = int(input())
sum1, sum2 = 0, 0
for i in range(N):
    for j in range(N):
        if i < j:
            sum1 += a[i][j]
        elif i > j:
            sum2 += a[i][j]
sum = int(math.fabs(sum1 - sum2))
if sum <= K:
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
