import math

def thuannghich(n):
    s = str(n)
    s1 = s[::-1]
    if s == s1 and len(s)>=2:
        return True
    return False

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
        if a[i][j] > max and thuannghich(a[i][j]):
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
# 23 21 77 10
# 13 13 22 14
# 28 29 28 23
# 29 77 11 19
# 16 26 24 21
# 13 25 77 77

