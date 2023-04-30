quan = int(input())
somaS1, somaB1, somaA1, somaS2, somaB2, somaA2 = 0, 0, 0, 0, 0, 0

for i in range(quan):
    nome = input()
    jogada1 = input().split()
    jogada2 = input().split()
    saque = int(jogada1[0])
    bloqueio = int(jogada1[1])
    ataque = int(jogada1[2])
    saque2 = int(jogada2[0])
    bloqueio2 = int(jogada2[1])
    ataque2 = int(jogada2[2])
    somaS1 += saque
    somaB1 += bloqueio
    somaA1 += ataque
    somaS2 += saque2
    somaB2 += bloqueio2
    somaA2 += ataque2

print(f'Pontos de Saque: {((somaS2 / somaS1) * 100.0):.2f} %.')
print(f'Pontos de Bloqueio: {((somaB2 / somaB1) * 100.0):.2f} %.')
print(f'Pontos de Ataque: {((somaA2 / somaA1) * 100.0):.2f} %.')