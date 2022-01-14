t = int(input())
while t>0:
    N = int(input())
    a = [int(x) for x in input().split()]
    ans = []
    for i in range(N):
        if len(ans)==0:
            print(1,end=' ')
        else:
            while len(ans)>0 and a[i] >= a[ans[len(ans)-1]]:
                ans.pop()
            if len(ans)==0:
                print(i+1,end = ' ')
            else :
                print(i-ans[len(ans)-1],end = ' ')
        
        ans.append(i)
    print()
    t-=1
# 1
# 7
# 100 80 60 70 60 75 85