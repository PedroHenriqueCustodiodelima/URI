qC = int(input())

for i in range(qC):
    nomeCompetidor = input()
    gD = float(input())
    notas = input().split()
    arrNotas = [float(nota) for nota in notas]
    arrNotas.remove(min(arrNotas))
    arrNotas.remove(max(arrNotas))
    soma = sum(arrNotas)
    print(f"{nomeCompetidor} {soma*gD:.2f}")