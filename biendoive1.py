while True :
    N = int(input())
    if(N==0) : break
    index =1
    while N!=1 :
        if N%2==0 :
            N/=2
        else : N = N*3+1
        index+=1
    print(index)
