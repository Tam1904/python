import math
t = int(input())
while t > 0:
    N = int(input())
    count = 0
    for i in range(N):
        if math.gcd(i, N) == 1 :
            count += 1
    if count < 2:
        print("NO")
    else:
        OK = 1
        for i in range(2, int(math.sqrt(count))+1):
            if count % i == 0:
                print("NO")
                OK = 0
                break
        if OK == 1:
            print("YES")
    t-=1
