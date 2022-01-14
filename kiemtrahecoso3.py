t = int(input())
while t>0:
    s = str(input())
    try:
        number = int(s,3)
        print('YES')
    except :
        print('NO')
    t-=1