import math
t = int(input())
while t>0:
    n = int(input())
    sum =0
    while n>0 :
        sum+=n%10
        n//=10
    OK=0
    if sum <2 :
        print("YES")
    else :  
        for i in range(2,int(math.sqrt(sum))+1) :
             if sum%i==0 :
                 print("NO")
                 OK=1
                 break
        if OK ==0 : 
            print("YES")
    t-=1