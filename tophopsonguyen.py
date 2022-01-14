[N,M] = [int(x) for x in input().split()]
a = set(sorted([int(x) for x in input().split()]))
b = set(sorted([int(x) for x in input().split()]))
c = list(a&b)
print(sorted(c))
c = list(a-b)
print(sorted(c))
c = list(b-a)
print(sorted(c))
# 5 6
# 1 2 3 4 5
# 3 4 5 6 7 8