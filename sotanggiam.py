t = int(input())
while t>0:
    s = str(input())
    if len(s)<3:
        print("NO")
    else:
        OK=1
        j=0
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                print("NO")
                OK=0
                break
            if s[i] > s[i+1]:
                j =i
                break
        if OK==1:
            for i in range(j,len(s)-1):
                if s[i]<=s[i+1]:
                    print("NO")
                    OK=0
                    break
        if OK==1:
            print("YES")   
    t-=1
# 3
# 12
# 23342
# 5678961