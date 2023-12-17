while True:
    K = int(input())
    if K == 0:
        break

    N, M = map(int, input().split())

    for _ in range(K):
        X, Y = map(int, input().split())
        dX = X - N
        dY = Y - M

        if not dX or not dY:
            print("divisa")
        elif dX < 0 and dY > 0:
            print("NO")
        elif dX > 0 and dY > 0:
            print("NE")
        elif dX < 0 and dY < 0:
            print("SO")
        elif dX > 0 and dY < 0:
            print("SE")