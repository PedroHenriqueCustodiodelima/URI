n = int(input())

for i in range(n):
    J = 0
    M = J
    for j in range(3):
        x = input().split()
        J += int(x[0]) * int(x[1])
    for k in range(3):
        x = input().split()
        M += int(x[0]) * int(x[1])
    if J > M:
        print("JOAO")
    else:
        print("MARIA")
