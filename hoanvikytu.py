import itertools
ans = list(itertools.permutations(list(str(input()))))

for li in ans:
    for i in li:
        print(i,end = '')
    print()

# s = list(str(input()))
# n = len(s)
# vs = [0]*n
# ans = [0]*n
# def truy(i):
#     for j in range(n):
#         if vs[j]==0:
#             vs[j] =1
#             ans[i] = j
#             if i==n-1:
#                 for k in range (n):
#                     print(s[ans[k]],end = '')
#                 print()
#             elif i < n-1 :
#                 truy(i+1)
#             vs[j]=0

# truy(0)
                
            