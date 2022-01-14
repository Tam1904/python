N = int(input())
a =[int(x) for x in input().split()]
count=0
for i in range(N-1):
    if a[i]!=a[i+1] :
        count+=1
print(count)
# 6
# 1 0 0 1 1 1