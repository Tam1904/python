t = int(input())
while t>0:
    n = int(input())
    sum =0
    while n>0 :
        sum+=n%10
        n//=10
    s1 = str(sum)
    s2 = s1[::-1]
    if(len(s1)==1) :
        print("NO")
    elif s1==s2 :
        print("YES")
    else :
        print("NO") 
    t-=1