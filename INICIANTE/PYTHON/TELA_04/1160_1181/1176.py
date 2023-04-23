primeiro = 0
segundos = 1
proximo = 0
j = int(input())
for i in range(j):
    n = int(input()) + 1
    primeiro = 0
    segundos = 1
    for p in range(n):
        if p <= 1:
            proximo = p
        else:
            proximo = primeiro + segundos
            primeiro = segundos
            segundos = proximo
    print(f"Fib({n - 1}) = {proximo}")
