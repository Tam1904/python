import math
def check(n):
    if n<2 :
        return False
    for i in range(2,int(math.sqrt(n))+1) :
        if n%i==0 :
            return False
    return True

t = int(input())
while t>0:
    s = str(input())
    number1 = s.count('2') + s.count('3')+ s.count('5') + s.count('7') 
    if number1 > len(s)- number1  and check(len(s)) :
        print("YES")
    else :
        print("NO")
    t-=1