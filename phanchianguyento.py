import math
def check(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0 :
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if i not in b :
        b.append(i)
sum1 = sum(b)
tong,OK=0,0
for i in range(len(b)):
    tong+=b[i]
    if check(tong) and check(sum1-tong):
        OK=1
        print(i)
        break
if OK==0 :
    print("NOT FOUND")
