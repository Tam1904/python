class Thisinh:
    def __init__(self,ten,ngaysinh,diem1,diem2,diem3):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        
    def tongDiem(self):
        return self.diem1 + self.diem2 + self.diem3
    
    def __str__(self) :
        return f'{self.ten} {self.ngaysinh} {self.tongDiem():.1f}'
    
thiSinh = Thisinh(str(input()),str(input()),float(str(input())),float(str(input())),float(str(input())))
print(thiSinh)
# Nguyen Hoang Ha
# 11/10/2001
# 4.5
# 10.0
# 5.5