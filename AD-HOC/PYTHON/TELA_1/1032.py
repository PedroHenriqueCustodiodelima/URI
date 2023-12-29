def josephus(n):
    retorno = 0
    for i in range(1, n + 1):
        retorno = (retorno + primos[n - i]) % i
    return retorno + 1

def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0 or x < 2:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def preenche_primo():
    primos = []
    i = 2
    while len(primos) < MAXSIZE:
        if is_prime(i):
            primos.append(i)
        i += 1
    return primos

MAXSIZE = 3502
MAXPRIME = 32650
primos = preenche_primo()

while True:
    n = int(input())
    if n == 0:
        break
    print(josephus(n))
