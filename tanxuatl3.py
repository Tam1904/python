t = int(input())
while t>0:
    N = int(input())
    a = [int(x) for x in input().split()]
    b = set(a)
    for i in b :
        if a.count(i)%2==1 :
            print(i)
            break
    t-=1