runas_existentes, amizade_necessaria = map(int, input().split())

letras_runas = []
valor_runas = []

for _ in range(runas_existentes):
    letra, valor = input().split()
    letras_runas.append(letra)
    valor_runas.append(int(valor))

runas_recitadas = int(input())
runas_recitadas_input = input().split()

valor_amizade = 0

for runa_atual in runas_recitadas_input:
    for j in range(runas_existentes):
        if runa_atual == letras_runas[j]:
            valor_amizade += valor_runas[j]

print(valor_amizade)

if valor_amizade >= amizade_necessaria:
    print("You shall pass!")
else:
    print("My precioooous")
