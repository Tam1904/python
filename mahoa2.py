while True : 
    s = [str(x) for x in input().split()]
    k = int(s[0])
    if k==0 : 
        break
    P = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","_","."]
    a = str(s[1])
    ans=''
    for i in range(len(a)) :  
        for j in range(len(P)) : 
            if a[i]==P[j] : 
                c = int((j+int(k))%28)
                break
        ans+=P[c]
    print(ans[::-1])