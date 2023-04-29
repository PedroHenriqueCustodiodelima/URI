while True:
    try:
        a = input()
        if not a:
            break
        horario = a.split(':')
        hora = int(horario[0])
        minuto = int(horario[1])
        atraso = ((hora+1)-8)*60 + minuto
        if hora < 7 or (hora == 7 and minuto == 0):
            print(f"Atraso maximo: 0")
        else:
            print(f"Atraso maximo: {atraso}")
    except EOFError:
        break
