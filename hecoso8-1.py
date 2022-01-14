s = str(input())
while len(s)%3!=0:
    s = '0' + s
for i in range(0,len(s),3):
    print(int(s[i:i+3],2),end = '')