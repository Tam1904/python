import math
t = int(input())
def check(number):
    if number <2:
        return False
    for i in range(2,int(math.sqrt(number)+1)):
        if number%i==0:
            return False
    return True
while t>0:
    s = str(input())
    a = int(s[len(s)-4:])
    if check(a):
        print("YES")
    else :print("NO")
    t-=1
# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999