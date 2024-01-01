while True:
    N = int(input())

    if N == 0:
        break
    else:
        ACUM = 0

        for i in range(1, N + 1):
            T, Q = map(int, input().split())

            if Q % 2 == 0:
                ACUM += Q
            else:
                ACUM += Q - 1

        print(ACUM // 4)
