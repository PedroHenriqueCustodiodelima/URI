while True:
    try:
        a = input()
        if not a:
            break
        n, q = map(int, a.split())
        p = []
        for i in range(n):
            p.append(int(input()))
        p.sort(reverse=True)
        for j in range(q):
            posicao = int(input())
            print(p[posicao - 1])
    except EOFError:
        break
