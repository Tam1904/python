# # from decimal import *
# # # class Student:
# # #     def __init__(self, ten, ma,lop):
# # #         self.ten = ten
# # #         self.ma = ma
# # #         self.lop = lop
        
# # #     def description_student(self):
# # #         print(self.ten, self.ma,self.lop, sep = ' ')
        
# # #     def description_object(self,mon):
# # #         print(f'Bạn đang học môn {mon}')

# # # stu = Student("Nguyen Van A","B19DCCN001","D19CN11")
# # # stu.description_student()
# # # stu.description_object("Java")

# # print(Decimal('0'))
# # class Rectangle:
# #     def __init__(self, x, y, color):
# #         self.x = x
# #         self.y = y
# #         self.mau = color.title()

# #     def check(self):
# #         if self.x > 0 and self.y > 0:
# #             return True
# #         return False

# #     def perimeter(self):
# #         return (self.x + self.y) * 2

# #     def area(self):
# #         return self.x * self.y

# #     def color(self):
# #         return self.mau


# # if __name__ == "__main__":
# #     arr = input().split()
# #     r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
# #     if r.check():
# #         print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
# #     else:
# #         print("INVALID")


# # # 1
# # # 10 2 red

# from fractions import Fraction

# # a = Fraction(6, 9)
# # b = Fraction(2, 3)
# # c = a+b
# # # c.numerator lấy phần tử
# # # c.denominator lấy phần mấu
# # print(c)

# # c = complex(2, 5)
# # d = complex(2, 5)
# # print(c**2)

# text = ""
# stopword = ""
# while True:
#     line = input()
#     if line.strip() == stopword:
#         break
#     text += "%s\n" % line
# print(text)

# s = input()
# print(s.split('!'))


print('a'-'b')