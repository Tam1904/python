import math
number = 505
F = [0]*number
F[0]=F[1]=1
for i in range(2,int(math.sqrt(number))+1) :
    if F[i]==0 :
        for j in range(i*i,number,i) :
            F[j]=1
def check(s) :
    for i in range(len(s)) :
        if F[i]==1 and (int(s[i]) ==2 or int(s[i])==3 or int(s[i])==5 or int(s[i])==7) :
            return False
        if F[i]==0 and int(s[i])!=2 and int(s[i])!=3 and int(s[i])!=5 and int(s[i])!=7 :
            return False
    return True


t = int(input())
while t > 0:
    s = str(input())
    if check(s):
        print("YES")
    else :
        print("NO")
    t -= 1
# 2
# 14239567
# 2314514535353