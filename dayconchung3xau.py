t = int(input())
while t>0:
    [N,M,K] = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    d = []
    OK =0
    i,j=0,0
    while i< N and j < M:
        if a[i] > b[j] :
            j+=1
        elif a[i]<b[j] :
            i+=1
        elif a[i]==b[j]:
            d.append(a[i])
            i+=1
            j+=1
    i,j=0,0
    while i<len(d) and j < K:
        if d[i] > c[j] :
            j+=1
        elif d[i]<c[j] :
            i+=1
        elif d[i]==c[j]:
            OK =1
            print(d[i],end=' ')
            i+=1
            j+=1
    if OK==0 :
        print("NO",end = ' ')
    print()
    t-=1
# 3
# 6 5 8
# 1 5 10 20 40 80
# 5 7 20 80 100
# 3 4 15 20 30 70 80 120
# 3 5 4
# 1 5 5
# 3 4 5 5 10
# 5 5 10 20
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9