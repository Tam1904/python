import math

def nt(n):
    if n <2 :
        return False
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True

[n,m] = [int(x) for x in input().split()]
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
ans = []
OK =0
max =-100
for i in range(n):
    for j in range(m):
        if a[i][j] > max and nt(a[i][j]):
            ans.clear()
            OK =1
            max = a[i][j]
            ans.append([i,j])
        elif a[i][j]==max:
            ans.append([i,j])
            
if OK ==0:
    print('NOT FOUND')
else:
    print(max)
    for i in ans:
        print(f'Vi tri [{i[0]}][{i[1]}]')

# 6 4
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29

