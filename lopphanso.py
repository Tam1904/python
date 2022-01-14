import math


class Phanso:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def toiGian(self):
        c = math.gcd(self.x,self.y)
        self.x//=c
        self.y//=c
        
    def __str__(self): 
        return f'{self.x}/{self.y}'

[x,y] = [int(z) for z in str(input()).split()]

ps = Phanso(x,y)
ps.toiGian()
print(ps) 
