s = str(input())
count1,count2= 0,0
print(len(s))
for i in range(len(s)) : 
    if(s[i]>="a" and s[i] <="z") : 
        count1+=1
    else : count2+=1
if(count1>=count2) : print(s.lower())
else : print(s.upper())