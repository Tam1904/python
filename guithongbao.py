
t = int(input())
while t>0:
    s = str(input())
    if len(s)<100:
        print(s)
    else :
        index = 98
        while True:
            if s[index].isspace():
                print(s[:index+1])
                break
            index-=1
    t-=1
# 2
# Can cu Ke hoach giang day – hoc tap hoc ky 1 nam hoc 2021 – 2022 Can cu ket qua thi hoc ky 2 va hoc ky phu ky he nam hoc 2020 – 2021
# Hoc vien Cong nghe Buu chinh Vien thong to chuc khai giang truc tuyen