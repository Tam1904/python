t = int(input())
while t>0:
    [n,m] = [int(x) for x in input().split()]
    x = [[int(x) for x in input().split()] for i in range (0,n)]
    h = [[int(x) for x in input().split()] for i in range (0,3)]
    y = [[0 for i in range(m-2)] for j in range(n-2)]
    sum =0
    for i1 in range(0,n-2):
        for j1 in range(0,m-2):
            for i in range(0,3):
                for j in range(0,3):
                    sum+=x[i1+i][j1+j]*h[i][j]
            y[i1][j1] = sum
            sum =0
    for i in range(0,len(y)):
        for j in range(0,len(y[i])):
            sum+=y[i][j]
    print(sum)
    t-=1
# 2
# 4 4
# 2 1 0 0
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 1 1 1
# 1 1 1
# 1 1 1