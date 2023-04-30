a1 = list(map(int, input().split()))
a1.sort()
a,b,c = a1
if(a+b<=c):
    print("Invalido")
else:
    if(a==b and b==c):
        tipo = "Valido-Equilatero"
    elif(a==b or b==c):
        tipo = "Valido-Isoceles"
    else:
        tipo = "Valido-Escaleno"
    if((pow(a,2)+pow(b,2))==pow(c,2)):
        p = 'S'
    else:
        p = 'N'
    print(tipo)
    print("Retangulo:",p)