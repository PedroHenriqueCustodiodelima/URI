def ehprimo(soma):
    if soma <= 1:
        return False
    for j in range(2, int(soma ** 0.5) + 1):
        if soma % j == 0:
            return False
    return True

while True:
    try:
        m = int(input())
    except EOFError:
        break

    v = []
    for _ in range(m):
        v.append(int(input()))

    n = int(input())
    soma = 0

    v.reverse()

    for i in range(0, len(v), n):
        soma += v[i]

    if soma != 1 and soma != 0 and ehprimo(soma):
        print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
    else:
        print("Bad boy! I’ll hit you.")