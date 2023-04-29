while True:
    t = int(input())
    if t == 0:
        break

    for i in range(t):
        n = int(input())
        pedidos = (2 * n) - 1 if (n - 1) % 2 == 0 else (2 * n) - 2
        print(pedidos)
