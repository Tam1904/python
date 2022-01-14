[N,M] = [int(x) for x in input().split()]
a= []
for i in range(N):
    b =[int(x) for x in input().split()]
    a.append(b)
if N>M:
    K=N-M
    c =[i*2 for i in range(K)]
    for i in range(N):
        if i not in c:
            for j in range(M):
                print(a[i][j], end = " ")
            print()
if N<M:
    K=M-N
    c =[i*2+1 for i in range(K)]
    for i in range(N):
        for j in range(M):
            if j not in c:
                print(a[i][j], end = " ")
        print()

if N==M :
    for i in range(N):
        for j in range(M):
            print(a[i][j], end = " ")
        print()

# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9
# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7