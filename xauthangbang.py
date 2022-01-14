t = int(input())
while t > 0 :
    s = str(input())
    OK = 1
    p = "abcdefghijklmnopqrstuvwxyz"
    a = [abs(p.find(s[i])-p.find(s[i+1])) for i in range(len(s)-1)]
    s = s[::-1]
    b = [abs(p.find(s[i])-p.find(s[i+1])) for i in range(len(s)-1)]
    for i in range(len(a)) : 
        if a[i] != b[i] : 
            print("NO")
            OK =0
            break
    if OK==1 : print("YES")
    t-=1
