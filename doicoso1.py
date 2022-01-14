a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = int(input())
while t>0:
    [N,b] = [int(x) for x in input().split()]
    ans = []
    while N>0:
        ans.append(a[N%b])
        N//=b
    for i in range(len(ans)-1,-1,-1):
        print(ans[i],end= '')
    print()
    t-=1
