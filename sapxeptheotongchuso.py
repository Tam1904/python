def tong(n) :
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

def check(item) :
    sum = item[0]
    number = item[1]
    return (sum,number)
    
t = int(input())
while t>0:
    N = int(input())
    a = [[tong(int(x)),int(x)] for x in input().split()]
    a.sort(key=check)
    for i in a :
        print(i[1],end = ' ')
    print()
    t-=1
# 1
# 8
# 143 43 22 99 7 9 1111 10000000