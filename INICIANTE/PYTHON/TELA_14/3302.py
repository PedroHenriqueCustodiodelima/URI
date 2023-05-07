while True:
    try:
        n = int(input())
        for i in range(1, n+1):
            a = input()
            print(f"resposta {i}: {a}")
    except EOFError:
        break