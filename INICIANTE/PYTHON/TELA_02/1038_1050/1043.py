valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
if a < b + c and b < a + c and c < a + b:
    p = a + b + c
    print(f"Perimetro = {p:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")
