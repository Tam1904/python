t = int(input())
while t>0:
    a = str(input())
    mul=1
    for i in a:
        sum+=int(i)
    if sum%3==0 :
        print("YES")
    else :
        print("NO")
    t-=1