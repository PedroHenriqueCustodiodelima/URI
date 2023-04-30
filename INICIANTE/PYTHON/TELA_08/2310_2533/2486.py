while True:
    a = input()
    if a == "0":
        break
    t = int(a)
    consumo = 0
    for i in range(t):
        v = input().split()
        n = int(v[0])
        if v[1] == "suco":
            consumo += n * 120
        elif v[1] in ["morango", "mamao"]:
            consumo += n * 85
        elif v[1] == "goiaba":
            consumo += n * 70
        elif v[1] == "manga":
            consumo += n * 56
        elif v[1] == "laranja":
            consumo += n * 50
        elif v[1] == "brocolis":
            consumo += n * 34
    if consumo > 130:
        print(f"Menos {consumo - 130} mg")
    elif consumo < 110:
        print(f"Mais {110 - consumo} mg")
    else:
        print(f"{consumo} mg")
