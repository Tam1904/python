t = int(input())
F = [0]*100
F[1] = F[2] =1
for i in range (3,93) :
    F[i] = F[i-1]+ F[i-2]
while t>0 :
    [a,b] = [int(x) for x in input().split()]
    for i in range(a,b+1) : 
        print(F[i],end=' ')
    print()
    t-=1