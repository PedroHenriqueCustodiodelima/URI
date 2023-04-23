t = int(input())

for i in range(t):
    pa, pb, g1, g2 = map(float, input().split())
    d, e = pa, pb
    n = 0
    while d <= e:
        d += int(d * (g1 / 100))
        e += int(e * (g2 / 100))
        n += 1
        if n > 100:
            break
    if n > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{n} anos.")
