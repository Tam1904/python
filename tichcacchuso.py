t = int(input())
while t>0:
    a = str(input())
    mul=1
    for i in a:
        if i !='0':
            mul*=int(i)
    print(mul)
    t-=1