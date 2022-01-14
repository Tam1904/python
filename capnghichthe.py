n = int(input())
a= []
count =0
m =input()
m= m.split()
for tu in m : 
    a.append(int(tu))
for i in range(n-1) :
    for j in range(i+1,n) :
        if a[i] > a[j] : count+=1
print(count)
