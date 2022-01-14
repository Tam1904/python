[n, m] = [int(x) for x in input().split()]

a = [int(x) for x in input().split()]

a.sort()
max1 = -1
max2 = -1
for i in range(n):
    if(a.count(a[i]) > a.count(max1)):
        max1 = a[i]
for i in range(n):
    if(a.count(a[i]) > a.count(max2) and a.count(a[i]) < a.count(max1)):
        max2 = a[i]
if max2 == -1:
    print("NONE")
else:
    print(max2)
