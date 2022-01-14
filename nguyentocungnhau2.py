import math
[N,K] = [int(x) for x in input().split()]
index =0
for i in range(10**(K-1),10**(K)):
    if math.gcd(i,N)==1 :
        index+=1
        print(i,end = " ")
        if index == 10 :
            print()
            index=0