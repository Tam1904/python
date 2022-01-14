import math
def check(n) :
    for i in range(2,int(math.sqrt(n)+1)) :
        if n%i==0 :
            return False
    return True

t = int(input())
while t>0:
    s = str(input())
    number1 = int(s[:3])
    number2 = int(s[-3:])
    if check(number1) and check(number2) :
        print("YES")
    else :
        print("NO")
    t-=1
# 3
# 12743
# 7337
# 12345678901234