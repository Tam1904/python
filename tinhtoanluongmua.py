import math
import datetime
class Tram:
    def __init__(self,ma,ten,thoigian,luongmua) :
        self.ma = ma
        self.ten = ten
        self.thoigian = thoigian
        self.luongmua = luongmua
        
    def setThoigian(self,time):
        self.thoigian+= time
    def setLuongmua(self,luongmua):
        self.luongmua+=luongmua
        
    def trungBinh(self):
        return (self.luongmua/self.thoigian)*3600
    
    def __str__(self):
        return '{} {} {:.2f}'.format(self.ma,self.ten,self.trungBinh())
    
t = int(input())
a = {}
index =1
for i in range(1,t+1):
    ma = 'T{:02d}'.format(index)
    ten = str(input())
    time1 = datetime.datetime.strptime(str(input()),'%H:%M')
    time2 = datetime.datetime.strptime(str(input()),'%H:%M')
    luongmua = int(input())
    if ten in a:
        a[ten].setThoigian((time2-time1).seconds)
        a[ten].setLuongmua(luongmua)
    else:
        index+=1
        tram = Tram(ma,ten,(time2-time1).seconds,luongmua)
        a[ten] = tram

for tram in a:
    print(a[tram])
        
      
# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35