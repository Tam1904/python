P = ["000","001","010","011","100","101","110","111"]
s = str(input())
while len(s)%3!=0 :
    s= s+'0'
a = []
for i in range(0,len(s),3) :
    tmp = s[i:i+3]
    a.append(P.index(tmp))
print(a)