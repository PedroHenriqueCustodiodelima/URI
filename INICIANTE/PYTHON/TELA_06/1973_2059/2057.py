entrada = input().split()
saida = int(entrada[0])
tempo = int(entrada[1])
fuso = int(entrada[2])
destino = saida + tempo + fuso

if destino > 23:
    destino = destino - 24
if destino < 0:
    destino = destino + 24

print(destino)
