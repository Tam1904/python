import math
t = int(input())
while t>0:
    s = str(input())
    s2 = s[::-1]
    number1 = int(s)
    number2 = int(s2)
    if math.gcd(number1,number2)==1 :
        print("YES")
    else :
        print("NO")
    t-=1
# 2
# 123
# 997