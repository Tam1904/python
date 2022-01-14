N = int(input())
a = [float(x) for x in input().split()]
min1 = min(a)
max1 = max(a)
count1 = a.count(min1)
count2 = a.count(max1)
sum1 = sum(a)
d = (sum1-count1*min1-count2*max1)/(len(a)-count1-count2)
print(format(d,'.2f'))
# 6
# 6.75 8 9.2 7.25 7.75 6.75