import math

while True:
    try:
        volume = float(input())
        diametro = float(input())
        area = 3.14 * (diametro / 2) ** 2
        altura = volume / area
        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")
    except:
        break
