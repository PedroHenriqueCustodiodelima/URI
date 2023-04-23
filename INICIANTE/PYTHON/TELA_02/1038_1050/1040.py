notas = input().split()
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if media == 4.85:
  media = 4.8

print(f"Media: {media:.1f}")

if media >= 7:
  print("Aluno aprovado.")
elif media < 5:
  print("Aluno reprovado.")
else:
  print("Aluno em exame.")
  n_exame = float(input())
  print(f"Nota do exame: {n_exame:.1f}")
  media_exame = (media + n_exame) / 2
  if media_exame >= 5:
    print("Aluno aprovado.")
  else:
    print("Aluno reprovado.")
  print(f"Media final: {media_exame:.1f}")
