import math
def check(s) :
    sum=0
    for i in range(0,len(s),2) :
        sum+=int(s[i])
        if i<len(s)-1 : sum+=int(s[i+1])
        if int(s[i])%2==1 :
            return False
        if i< len(s)-1 and int(s[i+1])%2==0 :
            return False 
    for i in range(2,int(math.sqrt(sum))+1) :
        if sum%i==0 :
            return False
    return True
t = int(input())
while t > 0:
    s = str(input())
    if check(s) :
        print("YES")
    else :
        print("NO")
    t -= 1
# 2
# 2345678521
# 1212121212121212121212121