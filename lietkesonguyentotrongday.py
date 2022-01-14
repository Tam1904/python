import math
N = (int)(input())
a = [int(x) for x in input().split()]
max = 1000005
F = [0]*max
F[0]=F[1]=1
for i in range(2, (int)(math.sqrt(max))):
    if F[i] == 0:
        for j in range(i*i, max,i):
            F[j] = 1
dic = {}
for i in a : 
    if i not in dic :
        dic[i] = 1
    else : 
        dic[i] = dic[i] +1
for key,value in dic.items() : 
    if F[key]==0 :
        print(key,value)
# 10
# 2 4 7 5 7 8 9 3 7 2