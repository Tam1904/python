s = str(input())
number = len(s)
while number-3 >0 :
    s = s[:number-3] + ',' + s[number-3:]
    number-=3
print(s)