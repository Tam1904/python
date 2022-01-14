t = int(input())
for i in range(1,t+1) : 
    s1 = input()
    s2 = input()
    a = list(s1)
    a.sort()
    b = list(s2)
    b.sort()
    print(f"Test {i}: ",end = ' ')
    if ''.join(map(str,a)) == ''.join(map(str,b)) :
        print("YES")
    else :
        print("NO")