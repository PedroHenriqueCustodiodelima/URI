n, m = map(int, input().split())
x, y = 0, 0
matriz = [[int(j) for j in input().split()] for i in range(n)]
for k in range(n-2):
    for l in range(m-2):
        if matriz[k][l] == 7 and matriz[k][l+1] == 7 and matriz[k][l+2] == 7 and \
           matriz[k+1][l] == 7 and matriz[k+1][l+1] == 42 and matriz[k+1][l+2] == 7 and \
           matriz[k+2][l] == 7 and matriz[k+2][l+1] == 7 and matriz[k+2][l+2] == 7:
            x, y = k+2, l+2
print(x, y)
