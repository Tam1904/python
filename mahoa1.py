# t = int(input())
# while t > 0:
#     s = str(input())
#     dic = {}
#     for i in s:
#         if i in dic:
#             dic[i] = dic[i] + 1
#         else:
#             dic[i] = 1

#     for key, value in dic.items():
#         print(value,key,sep=' ',end=' ')
#     print()
#     t -= 1
# # 3
# # AACDDPQ
# # 11111147g
# # 1111111111

t = int(input())

while t>0:
    s = str(input())
    ans = ""
    count = 1
    for i in range(0,len(s)):
        if i+1 == len(s):
            ans += str(count) + s[i]
        elif s[i] == s[i+1]:
            count += 1
        else:
            ans += str(count) + s[i]
            count = 1
    print(ans)
    t-=1