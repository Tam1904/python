t = int(input())
P = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while t>0:
    [N,K] = [int(x) for x in input().split()]
    a = ''
    while N > 0 :
        number = N%K
        N//=K
        a+=P[number]
    
    print(a[::-1])
    t-=1
# 3
# 10 2
# 2021 2
# 31 16