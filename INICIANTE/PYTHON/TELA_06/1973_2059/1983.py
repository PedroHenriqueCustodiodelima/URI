alunos = int(input())
maior = 0
escolhido = ""
for aluno in range(alunos):
    linha = input().split(' ')
    matricula = linha[0]
    nota = float(linha[1])
    if nota > maior:
        maior = nota
        escolhido = matricula
if maior >= 8:
    print(escolhido)
else:
    print("Minimum note not reached")
