# from fractions import* 
# from decimal import* 
# # import fractions
# # import decimal
# t = int(input())
# getcontext().prec = 7
# while t>0:
#     a = Fraction(0,1)
#     N = int(input())
#     if N%2==0 :
#         for i in range(2,N+1,2) :
#             b = Fraction(1,i)
#             a = a + b
#         p = Decimal(a.numerator)/a.denominator
#         print(p)
#     else :
#         for i in range(1,N+1,2) :
#             b = Fraction(1,i)
#             a = a+b
#         p = Decimal(a.numerator)/a.denominator
#         print(p)
#     t-=1
t = int(input())
while t > 0:
    N = int(input())
    sum=0
    if N %  2 == 0:
        for i in range(2,N+1,2):
            sum += 1/i
        print(format(sum,'.6f'))
    else :
        for i in range(1,N+1,2):
            sum += 1/i
        print(format(sum,'.6f'))
    t-=1