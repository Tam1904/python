import math
t = int(input())
while t > 0:
    N = int(input())
    count = 0
    print("1 * ",end ='')
    for i in range(2, int(math.sqrt(N)+1)):
        while N % i == 0:
            N = int(N/i)
            count += 1
        if count > 0 and N>1 :
            print(i, count, sep='^', end=' * ')
            count = 0
        if count > 0 and N==1 :
            print(i, count, sep='^',end =' ')
            break
    if N >1 :
        print(N, 1, sep='^',end ='')
    print()
    t -= 1
# 3
