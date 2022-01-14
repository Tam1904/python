t = int(input())
while t>0 :
    [N,X,M] = [float(x) for x in input().split()]
    index =1
    while N+N*X/100 < M :
        N = N+N*X/100
        index+=1
    print(index)
    t-=1
# 2
# 200.00 6.5 300
# 500 4 1000.00