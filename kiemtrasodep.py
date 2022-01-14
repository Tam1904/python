t = int(input())
while t>0:
    s = str(input())
    set = {i for i in s}
    if len(set)!=2:
        print("NO")
    else:
        OK =1
        for i in range(0,len(s),2):
            if i+2<len(s) and s[i]!=s[i+2]  :
                OK=0
                break
        for i in range(1,len(s),2):
            if i+2 < len(s) and s[i]!=s[i+2] :
                OK=0
                break
        if OK==1:
            print("YES")
        else:
            print("NO")
                
    t-=1
# 3
# 12121212
# 343433
# 78789989