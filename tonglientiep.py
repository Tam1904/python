t = int(input())
while t>0:
    b =1
    count = 0
    n = int(input())
    while True:
        a = n/(b+1) - b/2
        c = int(a)
        if a <1:
            break
        if c-a ==0.0 :
            count+=1
        
        b+=1
    print(count)
    t-=1
