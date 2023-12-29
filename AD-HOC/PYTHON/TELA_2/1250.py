n = int(input())

for _ in range(n):
    x = int(input())
    cont = 0
    tiro = list(map(int, input().split()))
    pulo = input()

    for j in range(x):
        if pulo[j] == 'S' and tiro[j] < 3:
            cont += 1
        elif pulo[j] == 'J' and tiro[j] > 2:
            cont += 1

    print(cont)
