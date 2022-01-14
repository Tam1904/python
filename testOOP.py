class Rectangle:
    dai:int
    rong:int
    mausac:str
    def chuanhoa(self,s:str)->str:
        ans=s.strip().lower().split()
        ans[0]=ans[0].title()
        return ''.join(ans)
    def __init__(self,dai,rong,mauSac):
        self.dai=int(dai)
        self.rong=int(rong)
        self.mausac=self.chuanhoa(mauSac)
    def perimeter(self):
        ans = (self.dai+self.rong)*2
        return ans
    def area(self):
        ans= self.dai*self.rong
        return ans
    def color(self):
        return self.mausac

arr = input().split()
if int(arr[0])<=0 or int(arr[1])<=0:
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))