class KhachHang:
    
    def __init__(self,i,ten,soNuoc):
        self.ma = 'KH{:02d}'.format(i)
        self.ten = ten
        self.soNuoc = soNuoc
        
    def tongTien(self):
        if self.soNuoc > 100:
            return round(((50*100 + 50*150) + (self.soNuoc-100)*200)*1.05)
        if self.soNuoc > 50:
            return round((50*100 + (self.soNuoc-50)*150)*1.03)
        return round((self.soNuoc*100)*1.02)
    
    def __lt__(self,other):
        if self.tongTien() > other.tongTien():
            return True
        return False
    
    def __str__(self):
        return '{} {} {}'.format(self.ma,self.ten,self.tongTien())
khachHangs = []
t = int(input())
for i in range(1,t+1):
    khachHang = KhachHang(i,str(input()),-(int(input())-int(input())))
    khachHangs.append(khachHang)
khachHangs.sort()
for khachHang in khachHangs:
    print(khachHang)  
# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612