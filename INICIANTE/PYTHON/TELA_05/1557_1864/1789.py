while True:
    try:
        entrada = input()
        if entrada == "":
            break
        
        maior_velocidade = 0
        lesma = 0
        lesmas = int(entrada)
        velocidades = input().split()
        
        while lesmas > 0:
            velocidade_tartaruga = int(velocidades[lesma])
            if maior_velocidade < velocidade_tartaruga:
                maior_velocidade = velocidade_tartaruga
            lesmas -= 1
            lesma += 1
            
        if maior_velocidade >= 20:
            print("3")
        elif maior_velocidade >= 10 and maior_velocidade < 20:
            print("2")
        else:
            print("1")
            
    except EOFError:
        break
