t = int(input())
while t > 0:
    n = int(input())
    a = [int(x) for x in input().split()]
    dic = {}
    for i in range(n):
        key = a[i]
        if key in dic:
            dic[key] = dic[key] + 1
        else:
            dic[key] = 1

    OK = 0
    max_count =0
    res = -1
    for key, value in dic.items():
        if max_count < value :
            res = key
            max_count = value
    if max_count > n/2 : 
        print(res)
    else:
        print("NO")
    t -= 1
# 2
# 9
# 3 3 4 2 4 4 2 4 4
# 8
# 3 3 4 2 4 4 2 4