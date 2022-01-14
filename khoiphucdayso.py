n = int(input())
a = []
for i in range(n) :
    b = [int(x) for x in input().split()]
    a.append(b)
A =[0]*n
for i in range(1,n-1) : 
    A[i] = (int)((a[0][i]-a[0][i+1]+a[i][i+1])/2)
    A[i+1] = (int)(-(a[0][i]-a[0][i+1]-a[i][i+1])/2)
A[0] = a[0][n-1] - A[n-1]
for i in A : 
    print(i,end=' ')
