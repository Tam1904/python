a=[]
while len(a)<10:
    s1 = [int(x) for x in input().split()]
    a+=s1
b = set(i%42 for i in a)
print(len(b))
