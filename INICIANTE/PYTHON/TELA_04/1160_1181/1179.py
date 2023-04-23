par = []
impar = []
numeros = []
for i in range(15):
    numeros.append(int(input()))

    if numeros[i] % 2 == 0:
        if len(par) < 5:
            par.append(numeros[i])
        else:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par = [numeros[i]]

    else:
        if len(impar) < 5:
            impar.append(numeros[i])
        else:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar = [numeros[i]]

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")

for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")
