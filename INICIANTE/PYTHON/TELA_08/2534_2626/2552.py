while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    
    ma = []
    for i in range(n):
        ma.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(m):
            if ma[i][j]:
                print('9', end='')
            else:
                v = 0
                if i > 0:
                    v += ma[i-1][j]
                if j > 0:
                    v += ma[i][j-1]
                if i < n-1:
                    v += ma[i+1][j]
                if j < m-1:
                    v += ma[i][j+1]
                print(v, end='')
        print()
