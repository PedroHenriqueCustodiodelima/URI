while True:
  try:
    letras,vezes = map(int,input().split())
    chave_1 = input().lower()
    chave_2 = input().lower()
    chave_1_aux =chave_1.upper()
    chave_2_aux =chave_2.upper()
    saida = ''
   
    for i in range(vezes):
        texto = input()
        texto = list(texto)
       
        for j in range(len(texto)):
            for k in range(letras):
              #compara maiusculos
                if texto[j] == chave_1[k]:
                    texto[j] = chave_2[k]
               
                elif texto[j] == chave_2[k]:
                    texto[j] = chave_1[k]
                #compara minusculos
                elif texto[j] == chave_1_aux[k]:
                    texto[j] = chave_2_aux[k]
               
                elif texto[j] == chave_2_aux[k]:
                    texto[j] = chave_1_aux[k]
           
            saida += texto[j]
        print(saida)
        saida = ''
    print()
  except:
    break