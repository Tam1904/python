t = int(input())
a = []
while t>0:
    s = str(input())
    number =0
    s+=' '
    for i in range(len(s)):
        if s[i].isdigit():
            number = number*10 + int(s[i])
        else:
            if number>0:
                a.append(number)
                number =0
            elif number ==0 and s[i-1]=='0' and i>0:
                a.append(0)
    t-=1
a.sort()
for number in a:
    print(number)
# 3
# A129h
# G07bxjq3
# aaaaaaa4aaaa