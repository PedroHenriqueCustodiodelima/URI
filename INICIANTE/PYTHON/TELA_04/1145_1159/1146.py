n = int(input())
sequencia = ""
while n != 0:
    for i in range(1, n):
        sequencia += str(i) + " "
    sequencia += str(n)
    print(sequencia)
    sequencia = ""
    n = int(input())
