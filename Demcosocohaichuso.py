s = str(input())
dic ={}
for i in range(0,len(s)-1,2):
    number = int(s[i:i+2])
    if number in dic:
        dic[number]+=1
    else:
        dic[number]=1
for key,value in dic.items():
    print(key,value, sep=' ')