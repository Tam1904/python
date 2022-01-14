
t = int(input())
while t>0:
    s = str(input())
    sum =0
    mul =1
    OK=0
    for i in range(1,len(s)+1,2) :
        if i<len(s) :
            sum+=int(s[i])
        if int(s[i-1])!=0 :
            OK=1
            mul*=int(s[i-1])
    if OK ==0 :
        mul =0
    print(mul,sum,sep=' ')
    t-=1
# 3
# 12345678
# 20000
# 22334455667788