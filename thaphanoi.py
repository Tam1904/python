def tower(n,A,B,C):
    if n==1:
        print('{} -> {}'.format(A,C))
        return
    tower(n-1,A,C,B)
    tower(1,A,B,C)
    tower(n-1,B,A,C)

N = int(input())
tower(N,'A','B','C')