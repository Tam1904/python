t = int(input())
while t > 0:
    a = []
    b = []
    n = int(input())
    s = input()
    s = s.split()
    for tu in s:
        a.append(int(tu))
    s = input()
    s = s.split()
    for tu in s:
        b.append(int(tu))
    a.sort()
    b.sort()
    OK = 1
    for i in range(n):
        if(a[i] > b[i]):
            print("NO")
            OK = 0
            break
    if OK == 1:
        print("YES")
    t -= 1
