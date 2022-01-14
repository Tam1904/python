def check(items):
    a = items[1]
    b = items[0]
    return (a,b)
while True:
    N = int(input())
    if N==0 :
        break
    a = []
    for i in range(N) :
        s = str(input().lstrip('0'))
        a.append([s,len(s)])
    a.sort(key=check)
    if a[0][0] == a[len(a)-1][0]:
        print("BANG NHAU")
    else :
        print(a[0][0], a[len(a)-1][0],sep = ' ')
# 5
# 101
# 100
# 1000
# 101
# 5
# 3
# 001
# 200
# 33333333333333333333333333333333333
# 3
# 1
# 1
# 1
# 0
