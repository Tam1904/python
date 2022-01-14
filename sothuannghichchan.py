t = int(input())
a = ['2','4','6','8']
b = ['2','4','6','8']
while True:
    tmp = b[0]
    if len(tmp)==3:
        break
    b.remove(tmp)
    for i in ['0','2','4','6','8']:
        b.append(tmp + i)
        a.append(tmp+i)
        
for i in range(len(a)):
    s = a[i]
    a[i] = a[i] + s[::-1]
            
while t>0:
    N = int(input())
    for i in a:
        if int(i) < N:
            print(i,end = ' ')
    print()
    t-=1