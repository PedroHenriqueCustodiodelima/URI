soma = 0
sair = 0
maior = 1
menor = 1
while sair != 1:
    vetor = input().split()
    a = int(vetor[0])
    b = int(vetor[1])
    if a <= 0 or b <= 0:
        sair = 1
    else:
        if a > b:
            maior = a
            menor = b
        else:
            maior = b
            menor = a
        for c in range(menor, maior+1):
            soma += c
            print(c, end=' ')
        print("Sum={}".format(soma))
        soma = 0
