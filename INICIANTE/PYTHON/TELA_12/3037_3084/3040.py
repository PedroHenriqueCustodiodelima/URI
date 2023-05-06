n = int(input())
for i in range(n):
    x = input().split()
    x0 = int(x[0])
    x1 = int(x[1])
    x2 = int(x[2])
    if x0 >= 200 and x0 <= 300 and x1 >= 50 and x2 >= 150:
        print("Sim")
    else:
        print("Nao")
