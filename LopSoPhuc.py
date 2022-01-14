t = int(input())
while t>0:
    [a,b,c,d] = [int(x) for x in input().split()]
    x = complex(a,b)
    y = complex(c,d)
    z1 = (x+y)*x
    z2 = (x+y)**2
    thuc = int(z1.real)
    ao = int(z1.imag)
    if ao <0:
        print(f'{thuc} - {ao*-1}i,', end = ' ')
    else:
        print(f'{thuc} + {ao}i,',end=' ')
    thuc = int(z2.real)
    ao = int(z2.imag)
    if ao <0:
        print(f'{thuc} - {ao*-1}i')
    else:
        print(f'{thuc} + {ao}i')
    t-=1
# 3
# 1 2 3 4
# 2 3 4 5
# 1 -2 5 -6