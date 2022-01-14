# n = int(input())
# F = [0]*(n+5)
# while True:
#     s = str(input())
#     if s=='HELP':
#         for i in range(1,n+2):
#             if F[i]==1:
#                 print(i, end = ' ')
#         break
#     b = [int(x) for x in s.split()]
#     s2 = str(input())
#     if s2=='YES':
#         for so in b:
#             F[so] =1
#     else :
#         for so in b:
#             F[so] =0

# from datetime import datetime

# date_string = "7 March, 2019"
# print("date_string =", date_string)

# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print("date_object =", date_object)


# import datetime

# date_str = "10:40"
# date_format =  "%H:%M"

# dt = datetime.datetime.strptime(date_str,date_format)
# dt1 = datetime.datetime.strptime(date_str,date_format)
# print(type(dt))
# print(dt.strftime('%H:%M %p'))


# import datetime
# str1= "21/02/13"
# str2= "21/02/15"
# dt1 = datetime.datetime.strptime(str1, "%y/%m/%d")
# dt2 = datetime.datetime.strptime(str2, "%y/%m/%d")
# dt3 = dt2 - dt1
# print(type(dt3))
# print(dt3.days)
# td_day= (dt1-dt2).days
# if td_day > 0:
#     print(dt1," lon hon ",dt2)
# elif td_day < 0:
#     print(dt1," nho hon ",dt2)
# else:
#     print(dt1, " bang ",dt2)
# print(datetime.timedelta(seconds=666))
import time

# print(time.strftime("%H gio %M phut %S giay", time.gmtime(666)))
# print(time.gmtime(66).tm_min)
# str_format = "{} is {:03d} years old".format('Kiyoshi',30)
# print(str_format)

print(10/3)