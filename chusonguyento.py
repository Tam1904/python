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
    if not check(len(s)):
        print("NO")
    else:
        dem1,dem2=0,0
        for i in s:
            if i not in ['2','3','5','7']:
                dem1+=1
            else:
                dem2+=1
        if dem2>dem1:
            print('YES')
        else:
            print('NO')
    t-=1
# 3
# 1234567
# 22334455667
# 23400300489898989