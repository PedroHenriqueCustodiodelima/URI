produtos = int(input())
total = 0

for produto in range(produtos):
    linha = input().split()
    codigo = int(linha[0])
    quant = int(linha[1])

    if codigo == 1001:
        total += 1.5 * quant
    elif codigo == 1002:
        total += 2.5 * quant
    elif codigo == 1003:
        total += 3.5 * quant
    elif codigo == 1004:
        total += 4.5 * quant
    elif codigo == 1005:
        total += 5.5 * quant

print(f'{total:.2f}')
