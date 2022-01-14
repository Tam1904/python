n = int(input())
a = [int(x) for x in input().split()]
a.sort()
OK=0
for i in range(len(a)-1) :
    if a[i+1] - a[i] > 1 :
        OK=1
        print(a[i]+1)
        break;
if(OK==0) : print(a[n-1]+1)