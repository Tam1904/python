t = int(input())
while t>0:
    s1 = str(input())
    s2 = str(input())
    len1 = len(s2)
    count,i=0,0
    while i < len(s1):
        if s1[i:i+len1]==s2:
            count+=1
            i+=len1
        else:
            i+=1
    print(count)
    t-=1
# 2
# 1212121112211221121
# 121
# 2222222222322292
# 2222