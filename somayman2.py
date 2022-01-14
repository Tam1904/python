t = int(input())
while t > 0:
    N = str(input())
    count1 = N.count('4')
    count2 = N.count('7')
    if(count1 + count2 == len(N)):
        print("YES")
    else :
        print("NO")
    t -= 1
