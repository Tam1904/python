import math
[N, M] = [int(x) for x in input().split()]
A = [0]*10
A[0] =1
def truy(t, i):
    for j in range(t, M+1):
        A[i] = j
        if i == 3:
            if math.gcd(A[1], A[3]) == 1 and math.gcd(A[2], A[3]) == 1 and math.gcd(A[1], A[2]) == 1:
                print(f"({A[1]}, {A[2]}, {A[3]})")
        elif math.gcd(A[i], A[i-1]) == 1:
            truy(j+1, i+1)


truy(N, 1)
