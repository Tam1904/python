t = int(input())
a = [(0,1.0),(3,2.5),(5,3.0),(7,3.5),(10,4.0),(13,4.5),(16,5.0),(20,5.5),(23,6.0),(27,6.5),(30,7.0),(33,7.5),(35,8.0),(37,8.5),(39,9.0)]
while t>0:
    [r,l,s,w] = [float(x) for x in input().split()]
    diem1 = 9.0
    for i in range(len(a)-1):
        number1 = a[i][0]
        number2 = a[i+1][0]
        if number1 <=r <number2:
            diem1 = a[i][1]
            break
    diem2 = 9.0
    for i in range(len(a)-1):
        number1 = a[i][0]
        number2 = a[i+1][0]
        if number1 <=l <number2:
            diem2 = a[i][1]
            break
    diem = (diem1 + diem2 + s + w)/4
    du = diem - int(diem)
    if du >= 0.75:
        du = 1.0
    elif du >= 0.25 and du <=0.75:
        du = 0.5
    else:
        du = 0.0
    diem = int(diem) + du
    print(diem)
    t-=1
# 2
# 15 25 5.0 5.5
# 22 32 6.0 6.0