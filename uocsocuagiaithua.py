t = int(input())

while t > 0:
    n,p = [int(x) for x in input().split()]
    count = 0
    while n > 0:
        count += n // p
        n //= p
    print(count)
    t-=1