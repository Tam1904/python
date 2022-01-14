t = int(input())
while t>0:
    s= str(input())
    a = list(s)
    a.sort()
    sum,i=0,0
    while True :
        if a[i] >= '0' and a[i] <= '9' :
            sum+=int(a[i])
            i+=1
        else :
            break
    b = ''.join(map(str,a[i:])) + str(sum)
    print(b)
    t-=1
# 2
# AC2BEW3
# ACCBA10D2EW30