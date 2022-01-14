s = str(input())
K = int(input())
dic ={}
for i in range(0,len(s)-1,2):
    number = int(s[i:i+2])
    if number in dic:
        dic[number]+=1
    else:
        dic[number]=1
OK=0
for key in sorted(dic.keys()):
    if dic[key]>=K:
        OK=1
        print(key, dic[key], sep = ' ')
if OK==0 :
    print("NOT FOUND")
# 124356141111434356149
# 2