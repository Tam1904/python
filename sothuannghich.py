[a, b, M] = [int(x) for x in input().split()]


def checkcoso(number, coso):
    ans = []
    while number > 0:
        ans.append(number% coso)
        number //= coso
    l = 0
    r = len(ans) - 1
    while l < r:
        if ans[l] != ans[r]:
            return False
        l += 1
        r -= 1
    return True


c = ["1"]
d = [0,1]

def chuyennhiphan(s):
    dem,sum = 0,0
    for i in range(len(s)-1,-1,-1):
        sum += int(s[i])*2**dem
        dem+=1
    return sum

while len(c[0]) < 11:
    tmp = c.pop(0)
    d.append(chuyennhiphan(tmp + tmp[::-1]))
    d.append(chuyennhiphan(tmp + "0" + tmp[::-1]))
    d.append(chuyennhiphan(tmp + "1" + tmp[::-1]))
    c.append(tmp + "0")
    c.append(tmp + "1")

d.sort()

count = 0

for number in d:
    if number > b:
        break
    elif number < a:
        continue
    else:
        check_number = True
        for coso in range(2, M+1):
            if not checkcoso(number,coso):
                check_number = False
                break
        if check_number:
            count += 1
print(count)
