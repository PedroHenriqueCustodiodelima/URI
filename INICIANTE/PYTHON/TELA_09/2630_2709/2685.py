while True:
  try:
    graus = int(input())
    if graus < 90:
      print("Bom Dia!!")
    elif graus < 180:
      print("Boa Tarde!!")
    elif graus < 270:
      print("Boa Noite!!")
    elif graus < 360:
      print("De Madrugada!!")
    else:
      print("Bom Dia!!")
  except:
    break
