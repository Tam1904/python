s = str(input())
a = []
for i in range(0,len(s)-1,2):
    number = int(s[i:i+2])
    if number not in a:
        a.append(number)
# a.sort()
for i in a:
    print(i, end = " ")