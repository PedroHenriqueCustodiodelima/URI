valores = input().split()
a = int(valores[0])
i = 1
n = int(valores[i])

while n <= 0:
    i += 1
    n = int(valores[i])

soma = 0

for i in range(n):
    soma += a + i

print(soma)
