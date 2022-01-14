while True:
    a = [int(x) for x in input().split()]
    if a[0] == a[1] and a[1] == a[2] and a[2] == a[3] and a[0] == 0:
        break
    ans = 0
    while not (a[0] == a[1] and a[1] == a[2] and a[2] == a[3]):
        ans += 1
        a = [abs(a[i] - a[i+1]) if i < 3 else abs(a[3] - a[0]) for i in range(4)]
    print(ans)