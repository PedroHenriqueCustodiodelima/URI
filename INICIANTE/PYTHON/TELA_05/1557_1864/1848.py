valor = 0
cont = 0

while cont < 3:
    codigo = input()
    if codigo == "---*":
        valor += 1
    elif codigo == "--*-" :
        valor += 2
    elif codigo == "-**-":
        valor += 3
    elif codigo == "*--":
        valor += 4
    elif codigo == "*-*":
        valor += 5
    elif codigo == "**-":
        valor += 6
    elif codigo == "***":
        valor += 7
    else:
        print(valor)
        valor = 0
        cont += 1
