valores = input().split()
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

if a < b and a < c:
  menor = a
  if b < c:
    meio = b
    maior = c
  else:
    meio = c
    maior = b
elif b < c:
  menor = b
  if a < c:
    meio = a
    maior = c
  else:
    meio = c
    maior = a
else:
  menor = c
  if a < b:
    meio = a
    maior = b
  else:
    meio = b
    maior = a

print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)
