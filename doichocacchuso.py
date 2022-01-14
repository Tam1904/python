t =int(input())
while t>0:
    s = str(input())
    s = list(s)
    OK =0
    index1,index2 = -1,-1
    for i in range(len(s)-1,0,-1):
        tmp = s[i]
        index1 = i
        for j in range(len(s)-1,i,-1):
            if s[j] < tmp :
                index2 = j
                OK =1
            if OK==1:
                break
        if(OK==1):
            break
    while s[index2] == s[index2-1]:
        index2-=1
    tmp = s[index1]
    s[index1] = s[index2]
    s[index2] = tmp
    s = ''.join(map(str,s))
    if OK ==1 and s[0]!= '0':
        print(s)
    else:
        print(-1)

    t-=1
# 4
# 354
# 999
# 100
# 11101

 