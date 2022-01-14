a = ["10","12","14","16","18","20","22","24","26","28"]
i =0
while len(a)>0 : 
    t = a[i]
    if(int(t)%2==0) : 
        a.remove(t)
    else : i+=1
print(a)