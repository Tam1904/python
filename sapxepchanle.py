N = int(input())
b= []
c =[]
a = [int(x) for x in input().split()]
while len(a) < N:
    a += [int(x) for x in input().split()]
for i in range(N) :
    if a[i]%2==0:
        b.append(a[i])
    else :
        c.append(a[i])
b.sort()
c.sort(reverse=True)
k1,k2=0,0
for i in range(N):
    if a[i]%2==0 :
        print(b[k1], end = ' ')
        k1+=1
    else :
        print(c[k2], end = ' ')
        k2+=1
# 10
# 1 2 3 4 5 6 7 7 9 6

