def magia_dano(magia):
    if magia == "fire":
        return 200
    elif magia == "water":
        return 300
    elif magia == "earth":
        return 400
    else:
        return 100

def magia_raio(magia, lv):
    if magia == "fire":
        if lv == "1":
            return 20
        elif lv == "2":
            return 30
        elif lv == "3":
            return 50
    elif magia == "water":
        if lv == "1":
            return 10
        elif lv == "2":
            return 25
        elif lv == "3":
            return 40
    elif magia == "earth":
        if lv == "1":
            return 25
        elif lv == "2":
            return 55
        elif lv == "3":
            return 70
    elif magia == "air":
        if lv == "1":
            return 18
        elif lv == "2":
            return 38
    return 60

def intercessao(cx, cy, raio, rx, ry, largura, altura):
    cDx = abs(cx - (rx + largura / 2))
    cDy = abs(cy - (ry + altura / 2))

    if (cDx > (largura / 2 + raio)) or (cDy > (altura / 2 + raio)):
        return False
    elif (cDx <= largura / 2) or (cDy <= altura / 2):
        return True
    else:
        return ((cDx - largura/2)**2 + (cDy - altura/2)**2) <= raio**2

t = int(input())
for i in range(t):
    posicao = list(map(int, input().split()))
    w, h, x0, y0 = posicao[0], posicao[1], posicao[2], posicao[3]
    ataque = input().split()
    magia, lv, cx, cy = ataque[0], ataque[1], int(ataque[2]), int(ataque[3])

    if intercessao(cx, cy, magia_raio(magia, lv), x0, y0, w, h):
        print(magia_dano(magia))
    else:
        print(0)
