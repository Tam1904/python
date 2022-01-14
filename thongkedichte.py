[n,m] = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(n)]
b = [[0 for j in range(m)] for i in range(n)]
x = [-1,-1,-1,0,1,1,1,0]
y = [-1,0,1,1,1,0,-1,-1]
for i in range(n):
    for j in range(m):
        if a[i][j]==-1:
            for k in range(8):
                x1,y1 = i+ x[k],j+y[k]
                # if x1>=0 and x1 <n and y1>=0 and y1<m and a[x1][y1]!=-1:
                if x1>=0 and x1 <n and y1>=0 and y1<m :
                    b[x1][y1]+=a[x1][y1]
                    
count =0            
for i in range(n):
    for j in range(m):
        count+=b[i][j]

print(count)
# 4 4
# 1 1 0 1
# 2 -1 4 5
# 0 0 0 0
# 1 0 2 1
# 4 4
# 1 1 0 1 
# 2 -1 4 5 
# 0 0 -1 0 
# 1 0 2 1