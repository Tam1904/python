import math

[n,m] = [int(x) for x in input().split()]
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
ans = []
OK =0
min1 = 10000000
max1 =-100
for i in a:
    min1 = min(min(i),min1)
    max1 = max(max(i),max1)
for i in range(n):
    for j in range(m):
        if a[i][j] == max1-min1 :
            OK =1
            max = a[i][j]
            ans.append([i,j])
if OK ==0:
    print('NOT FOUND')
else:
    print(max)
    for i in ans:
        print(f'Vi tri [{i[0]}][{i[1]}]')

# 6 4
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 67 11 19
# 16 26 24 21
# 13 25 77 77

