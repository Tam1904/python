import math
t = int(input())
while t>0:
    s = str(input())
    s1 = s[::-1]
    OK=1
    for i in range(0,len(s)-1):
        if math.fabs(ord(s[i])-ord(s[i+1])) != math.fabs(ord(s1[i]) - ord(s1[i+1])):
            print('NO')
            OK =0
            break
    if OK==1:
        print('YES')
    t-=1
# 2
# acxz
# bcxz