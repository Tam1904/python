n = int(input())
tho = [str(input()) for i in range(n)]
dem=0
i=0
ans = []
while i <len(tho)-1:
    if len(tho[i].split())==6:
        ans.append(1)
        for j in range(i+1,len(tho)):
            i = j
            if len(tho[j].split())==7:
                break
    
    if len(tho[i].split())==7:
        i+=4
        ans.append(2)
print(len(ans))
for i in ans:
    print(i)
# 12
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
# Mot canh hai canh lai ba canh
# Tran troc ban khoan giac chang lanh
# Canh bon canh nam vua chop mat
# Sao vang nam canh mong hon bay
# Minh ve minh co nho ta
# Muoi lam nam ay thiet tha man nong
# Minh ve minh co nho khong
# Nhin cay nho nui nhin song nho nguon
    