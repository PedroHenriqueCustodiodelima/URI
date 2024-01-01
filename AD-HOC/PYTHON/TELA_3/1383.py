def is_sudoku(matriz):
    for i in range(9):
        testador = [0] * 10
        for j in range(9):
            if testador[matriz[i][j]] != 0:
                return 'NAO'
            else:
                testador[matriz[i][j]] = 1

    for i in range(9):
        testador = [0] * 10
        for j in range(9):
            if testador[matriz[j][i]] != 0:
                return 'NAO'
            else:
                testador[matriz[j][i]] = 1

    for i in range(2, 9, 3):
        testador = [0] * 10
        for j in range(i - 2, i + 1):
            for k in range(i - 2, i + 1):
                if testador[matriz[j][k]] != 0:
                    return 'NAO'
                else:
                    testador[matriz[j][k]] = 1

    return 'SIM'


n = int(input())
for h in range(1, n + 1):
    teste = 0
    matriz = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        testador = [0] * 10
        for j in range(9):
            if testador[matriz[i][j]] != 0:
                teste = 1
            else:
                testador[matriz[i][j]] = 1

    for i in range(9):
        testador = [0] * 10
        for j in range(9):
            if testador[matriz[j][i]] != 0:
                teste = 1
            else:
                testador[matriz[j][i]] = 1

    for i in range(2, 9, 3):
        testador = [0] * 10
        for j in range(i - 2, i + 1):
            for k in range(i - 2, i + 1):
                if testador[matriz[j][k]] != 0:
                    teste = 1
                else:
                    testador[matriz[j][k]] = 1

    print(f"Instancia {h}")
    print("SIM" if not teste else "NAO")
    print()
