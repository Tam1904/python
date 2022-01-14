t = int(input())
while t > 0:
    a = []
    N = int(input())
    for i in range(N):
        a.append(int(input()))
    dic = {}
    a.sort()
    max1 = 0
    for i in a:
        if i in dic:
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
        if dic[i] > max1:
            max1 = dic[i]
            ans = i
    print(ans)
    t -= 1
# 3
# 3
# 999
# 999
# 19
# 4
# 13
# 333
# 333
# 13
# 3
# 11
# 12
# 13
