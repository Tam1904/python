t = int(input())
while t > 0:
    s = str(input())
    if len(s) % 2 == 0 or s[0] == s[1]:
        print("NO")
    else:
        s1 = set(s[::2])
        if len(s1) == 1:
            print("YES")
        else:
            print("NO")
    t -= 1


# 2
# 2324272921262
# 13141516
