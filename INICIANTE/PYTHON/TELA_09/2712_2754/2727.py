while True:
    try:
        n = int(input())
        for i in range(n):
            codigo = input().split()
            letra = chr(96 + (((len(codigo) - 1) * 3) + len(codigo[0])))
            print(letra)
    except EOFError:
        break
