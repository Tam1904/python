import math
t = int(input())
while t > 0:
    [a, b] = [int(x) for x in input().split()]
    temp = math.gcd(a, b)
    count = 0
    while temp > 0:
        count += temp % 10
        temp = int(temp/10)
    OK = 1
    if count < 2:
        print("NO")
    else: 
        for i in range(2, int(math.sqrt(count))+1):
            if count % i == 0:
                print("NO")
                OK = 0
                break
        if OK == 1:
            print("YES")
    t-=1
# 3
# 28 42
# 123 18
# 550 55
