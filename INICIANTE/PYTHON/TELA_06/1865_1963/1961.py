ganhar = True
linha1 = input().split()
pulo = int(linha1[0])
canos = int(linha1[1])
linha2 = input().split()
alturas = [int(i) for i in linha2]
for i in range(canos - 1):
    if abs(alturas[i+1] - alturas[i]) > pulo:
        ganhar = False
if ganhar:
    print("YOU WIN")
else:
    print("GAME OVER")
