while True:
    try:
        y = float(input())
    except EOFError:
        break

    x = int(y)
    horas = int((y * 240) / 3600) % 60
    minutos = int((y * 240) / 60) % 60
    segundos = int(y * 240) % 60

    if x >= 0 and x < 90 or x == 360:
        print("Bom Dia!!")
        print("{:02d}:{:02d}:{:02d}".format((horas + 6) % 24, minutos, segundos))
    elif x >= 90 and x < 180:
        print("Boa Tarde!!")
        print("{:02d}:{:02d}:{:02d}".format((horas + 6) % 24, minutos, segundos))
    elif x >= 180 and x < 270:
        print("Boa Noite!!")
        print("{:02d}:{:02d}:{:02d}".format((horas + 6) % 24, minutos, segundos))
    elif x >= 270 and x < 360:
        print("De Madrugada!!")
        print("{:02d}:{:02d}:{:02d}".format((horas + 6) % 24, minutos, segundos))
