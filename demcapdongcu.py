N = int(input())
a = []
for i in range(N) :
    a.append(str(input()))
b = N+1
C = [[0]*b,]*b
for i in range(0,b) :
    for j in range(i+1) :
        if i == j or j==0 :
            C[i][j]=1
        else :
            C[i][j] = C[i-1][j]+C[i-1][j-1]
for i in range(b) :
    print(C[i])
# ans,count =0,0
# for i in range(N):
#     count=0
#     for j in range(N) :
#         if a[i][j] == 'C':
#             count+=1
#     print(count)
#     ans +=C[count][2]
# print(ans)

# 4
# CC..
# C..C
# .CC.
# .CC.
# n = int(input())

# a = []
# for i in range(n):
#     s = str(input())
#     a.append(s)
# dem = 0
# count = 0
# for i in range(n):
#     dem = 0
#     for j in range(n):
#         if a[i][j] == 'C':
#             dem+=1
#     count += (dem*(dem-1))/2
# for i in range(n):
#     dem = 0
#     for j in range(n):
#         if(a[j][i] == 'C'):
#             dem +=1
#     count += (dem*(dem-1))/2
# print(int(count))