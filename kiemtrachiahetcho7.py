t = int(input())
while t>0:
    N = int(input())
    dem =0
    OK=0
    while True:
        if N%7==0:
            print(N)
            OK =1
            break
        if dem >1000:
            break
        a = str(N) 
        b = a[::-1]
        N +=int(b)
        dem+=1
    if OK==0:
        print(-1)
    t-=1
# 5
# 1
# 2
# 3
# 4
# 999999