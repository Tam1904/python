s = str(input())
if len(s)==1:
    print(s)
else:
    while len(s)>1:
        i = len(s)//2
        number1 = int(s[:i])
        number2 = int(s[i:])
        number = number1 + number2
        print(number)
        s = str(number)