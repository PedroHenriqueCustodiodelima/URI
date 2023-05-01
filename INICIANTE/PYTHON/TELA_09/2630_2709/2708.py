turistas = 0
veiculos = 0

v = input().split()
while v[0] != "ABEND":
    if v[0] == "SALIDA":
        veiculos += 1
        turistas += int(v[1])
    else:
        veiculos -= 1
        turistas -= int(v[1])
    v = input().split()

print(turistas)
print(veiculos)