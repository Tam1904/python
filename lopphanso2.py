import  math

class Phanso:
    def __init__(self,x,y) :
        self.x =x
        self.y =y
        
    def tong(self,p):
        tu = self.x * p.y + p.x*self.y
        mau = self.y*p.y
        c = math.gcd(tu,mau)
        return Phanso(tu//c,mau//c)
    
    def __str__(self) :
        return f'{self.x}/{self.y}'
    
[x1,y1,x2,y2] = [int(z) for z in str(input()).split()]
p1 = Phanso(x1,y1)
p2 = Phanso(x2,y2)

print(p1.tong(p2))