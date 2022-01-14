t = int(input())
while t > 0:
    s = input()
    OK = 0
    for i in range(len(s)-1):
        if(s[i] > s[i+1]):
            print("NO")
            OK = 1
            break
    if(OK == 0): print("YES")
    t=t-1;

