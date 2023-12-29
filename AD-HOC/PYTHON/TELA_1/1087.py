import math

while True:
    px1, py1, px2, py2 = map(int, input().split())
    resultado = 2
    x = abs(px1 - px2)
    y = abs(py1 - py2)

    if px1 == py1 == px2 == py2 == 0:
        break

    if px1 == px2 and py1 == py2:
        resultado = 0
        print(resultado)
    elif px1 == px2 and py1 != py2:
        resultado = 1
        print(resultado)
    elif px1 != px2 and py1 == py2:
        resultado = 1
        print(resultado)
    elif x == y:
        resultado = 1
        print(resultado)
    else:
        print(resultado)