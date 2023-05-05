T = int(input())
while T>0:
    A,B = map(int,input().split())
    A = A**B
    A = len(str(A))
    print(A)
    T-=1