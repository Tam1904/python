[t,K] = [int(x) for x in input().split()]
a = []
dict = {}

def sorter(item):
    key = item[0]
    value = -item[1]
    return (value,key)

def hasNumbers(s):
    return any(char.isdigit() for char in s)

while t>0:
    inp = str(input()).lower()
    s = ''
    for i in inp:
        if i.isdigit() or i.isalpha() or i.isspace() :
            s+=i
        else :
            s+=' '

    b = [str(x) for x in s.split()]
    for tu in b:
        if hasNumbers(tu):
            if tu in dict:
                dict[tu]+=1
            else :
                dict[tu]=1
    t-=1
for key,value in dict.items():
    a.append([key,value])
for i in sorted(a,key = sorter):
    if i[1]>=K:
        print(i[0],i[1],sep=' ')
# 3 
# PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
# Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
# voi muc ho tro 500000 dong/sinh vien PTIT.