n = input().split()
x = int(n[0])
y = int(n[1])
while x != y:
    if x < y:
        print("Crescente")
    else:
        print("Decrescente")
    n = input().split()
    x = int(n[0])
    y = int(n[1])
