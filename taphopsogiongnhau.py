[N,M] = [int(x) for x in input().split()]
a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
c = a - b
if len(c)==0:
    print("YES")
else :
    print("NO")
# 12 18
# 1 2 3 4 5 1 2 3 5 4 1 2
# 1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
