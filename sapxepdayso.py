t = int(input())
while t>0:
    [n,m] = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    index = a.index(max(a))
    a.insert(index,m)
    for i in range(len(a)):
        if a[i]<0:
            print(a[i],end = ' ')
    for i in range(len(a)):
        if a[i]>=0:
            print(a[i],end = ' ')
    print()
    t-=1
# 1
# 5 3
# -1 2 3 4 -1