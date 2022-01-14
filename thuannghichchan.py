t = int(input())
a = []


def sinh(b, i, n):
    for j in range(0, 10, 2):
        b[i] = j
        if i < n:
            sinh(b, i+1, n)
        else:
            c = b[0:n+1] + b[n::-1]
            if(c[0] != 0):
                a.append(''.join(map(str, c)))


b = [0]*6
for i in range(0, 3):
    sinh(b, 0, i)

while t > 0:
    s = input()
    for i in a:
        if int(i) < int(s):
            print(i, end=' ')
        else:
            break
    print()
    t -= 1
