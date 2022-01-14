import  math

class Matrix:
    def __init__(self,N,M,A) :
        self.N = N
        self.M = M
        self.A = A
        
    def chuyenvi(self):
        B = [[0 for j in range(self.N)] for i in range(self.M) ]
        # for i in range(self.M):
        #     C = []
        #     for j in range(self.N):
        #         C.append(0)
        #     B.append(C)
        for i in range(0,self.N):
            for j in range(0,self.M):
                B[j][i] = self.A[i][j]
        return Matrix(self.M,self.N,B)
    
    def tichChuyenvi(self,p):
        B = [[0 for j in range(p.M)] for i in range(self.N) ]
        # for i in range(self.N):
        #     C = []
        #     for j in range(p.M):
        #         C.append(0)
        #     B.append(C)
        for i in range(0,self.N):
            for j in range(0,p.M):
                sum=0
                for k in range (0,self.M):
                    sum+=self.A[i][k]*p.A[k][j]
                B[i][j] = sum
        return Matrix(self.N,p.M,B)
    
    def __str__(self):
        for i in range(0,self.N):
            for j in range(0,self.M):
                print(self.A[i][j],end = " ")
            print()
        return " "

t = int(input())
while t>0:
    [N,M] = [int(x) for x in input().split()]
    B = [[int(x) for x in input().split()] for i in range(N)]
    # for i in range(N):
    #     C = [int(x) for x in input().split()]
    #     B.append(C)
    matrix1 = Matrix(N,M,B)
    matrix2 = matrix1.chuyenvi()
    print(matrix1.tichChuyenvi(matrix2),end = ' ')        
    t-=1
# 1
# 2  2
# 1  2
# 3  4