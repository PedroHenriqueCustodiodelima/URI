n = int(input())

for i in range(n):
    x = int(input())
    sequenciaMaxima = 0
    sequenciaAtual = 0
    while x > 0:
        if x % 2 == 1:
            sequenciaAtual += 1
        else:
            if sequenciaAtual > sequenciaMaxima:
                sequenciaMaxima = sequenciaAtual
            sequenciaAtual = 0
        x //= 2
    if sequenciaAtual > sequenciaMaxima:
        sequenciaMaxima = sequenciaAtual
    print(sequenciaMaxima)
