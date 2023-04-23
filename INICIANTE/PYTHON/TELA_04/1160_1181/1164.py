n = int(input())
for i in range(n):
    k = 0
    x = int(input())
    for p in range(1, x):
        if x % p == 0:
            k += p
    if k == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
