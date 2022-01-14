s = str(input())
number = 1
while True :
    sum=0
    for i in s :
         sum += (ord(i) - ord('0'))
    if sum<10 :
        print(number)
        break
    number+=1
    s = str(sum)

