tipo = input()
matriz = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    matriz.append(linha)
total = 0
for i in range(12):
    for j in range(i):
        total += matriz[j][i]
if tipo == 'S':
    print("{:.1f}".format(total))
elif tipo == 'M':
    print("{:.1f}".format(total/66.0))
