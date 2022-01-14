N = int(input())
A = [[x for x in input()] for i in range(0,N)]
ans =0
for i in range(0,N):
    dem = A[i].count('C')
    ans +=(dem)*(dem-1)//2
for j in range(0,N):
    dem =0
    for i in range(0,N):
        if A[i][j] =='C':
            dem+=1
    ans +=(dem)*(dem-1)//2
print(ans)
# 4
# CC..
# C..C
# .CC.
# .CC.