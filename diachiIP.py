t = int(input())
while t>0:
    s = [str(x) for x in input().split('.')]
    a = []
    OK=1
    for i in s:
        try:
            number = int(i)
            a.append(number)
        except :
            OK=0
    if len(a)!=4:
        OK=0
    for i in a:
        if i>255 or i<0:
            OK=0
            break
    if OK==0:
        print('NO')
    else:
        print('YES')
    t-=1
# 2
# 192.168.1.1
# 256.255.255.255