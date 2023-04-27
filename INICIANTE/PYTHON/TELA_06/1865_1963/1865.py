n = int(input())

for i in range(n):
    texto = input().split(' ')
    nome = texto[0]
    forca = int(texto[1])
    if nome == "Thor":
        print("Y")
    else:
        print("N")