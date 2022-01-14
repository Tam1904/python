
class Rectangle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.mau = color.title()

    def check(self):
        if self.x > 0 and self.y > 0:
            return True
        return False

    def perimeter(self):
        return (self.x + self.y) * 2

    def area(self):
        return self.x * self.y

    def color(self):
        return self.mau


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
if r.check():
    print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")


# 1
# 10 2 red
