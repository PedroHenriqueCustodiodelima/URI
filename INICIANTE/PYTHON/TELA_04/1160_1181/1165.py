n = int(input())
for i in range(n):
    a = 0
    x = int(input())
    for p in range(1, x+1):
        if x % p == 0:
            a += 1
    if a == 2:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
