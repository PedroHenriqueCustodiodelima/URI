n = int(input())

coelho = 0
rato = 0
sapo = 0
soma = 0
rp = 0
cp = 0
sp = 0
vc = 0
vs = 0
vr = 0

for c in range(n):
    num, letra = input().split()

    if letra == "C":
        coelho += int(num)
    if letra == "S":
        sapo += int(num)
    if letra == "R":
        rato += int(num)
    soma += int(num)

sp = (sapo / soma) * 100.0
cp = (coelho / soma) * 100.0
rp = (rato / soma) * 100.0
vs = sp
vr = rp
vc = cp

print(f"Total: {soma} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print(f"Percentual de coelhos: {vc:.2f} %")
print(f"Percentual de ratos: {vr:.2f} %")
print(f"Percentual de sapos: {vs:.2f} %")
