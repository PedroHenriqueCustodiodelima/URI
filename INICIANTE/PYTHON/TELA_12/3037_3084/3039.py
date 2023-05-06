n = int(input())
bonecas = 0
carros = 0
for i in range(n):
    g = input().split()
    x = g[1]
    if x == "M":
        carros += 1
    else:
        bonecas += 1
print(f"{carros} carrinhos")
print(f"{bonecas} bonecas")