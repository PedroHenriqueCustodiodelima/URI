while True:
    try:
        frase = input().strip()
        if frase == "as duas":
            print("caiu")
        elif frase == "direita":
            print("frances")
        elif frase == "nenhuma":
            print("portugues")
        elif frase == "esquerda":
            print("ingles")
    except EOFError:
        break
