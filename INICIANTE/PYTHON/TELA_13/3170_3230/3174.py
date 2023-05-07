n = int(input())
B = 0
A = 0
M = 0
D = 0

for i in range(n):
    v = input().split(' ')
    t = v[1]
    horas = int(v[2])

    if t == "bonecos":
        B += horas
    elif t == "arquitetos":
        A += horas
    elif t == "musicos":
        M += horas
    else:
        D += horas

brin = (B // 8) + (A // 4) + (M // 6) + (D // 12)
print(brin)
