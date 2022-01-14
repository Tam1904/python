class HocSinh:
    
    def __init__(self,number,ten,bangdiem):
        self.ma = 'HS{:02d}'.format(number)
        self.ten = ten
        self.diem = self.xuLyDiem(bangdiem)
        
    def xuLyDiem(self,bangdiem):
        diem=0
        for i in range(len(bangdiem)):
            if i==0 or i ==1:
                diem +=bangdiem[i]*2
            else:
                diem+=bangdiem[i]
        diem/=12
        return round(round(diem,10),1)
    
    def xepLoai(self):
        if self.diem >=9.0:
            return 'XUAT SAC'
        if self.diem >=8.0:
            return 'GIOI'
        if self.diem >=7.0:
            return 'KHA'
        if self.diem >=5.0:
            return 'TB'
        return 'YEU'
    
    def __lt__(self,other):
        if self.diem > other.diem:
            return True
        if self.diem == other.diem and self.ma < other.ma:
            return True
        return False
    
    def __str__(self):
        return '{} {} {:.1f} {}'.format(self.ma,self.ten,self.diem,self.xepLoai())
    
hocSinhs = []
t = int(input())
for i in range(1,t+1):
    hocSinh = HocSinh(i,str(input()), [float(x) for x in input().strip().split()])
    hocSinhs.append(hocSinh)

hocSinhs.sort()
for hocSinh in hocSinhs:
    print(hocSinh)    

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0