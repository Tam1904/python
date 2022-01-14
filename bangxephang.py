class SinhVien:
    
    def __init__(self,ten,C,T):
        self.ten = ten
        self.C = C
        self.T = T
        
    def __lt__(self,other):
        if self.C >other.C:
            return True
        if self.C == other.C and self.T <other.T:
            return True
        if self.C == other.C and self.T == other.T and self.ten <other.ten:
            return True
        return False
    
    def __str__(self):
        return '{} {} {}'.format(self.ten,self.C,self.T)
    
listSV = []

t = int(input())
while t>0:
    ten = str(input())
    [C,T] = [int(x) for x in input().split()]
    sinhVien = SinhVien(ten,C,T)
    listSV.append(sinhVien)
    t-=1
listSV.sort()
for sinhVien in listSV:
    print(sinhVien)