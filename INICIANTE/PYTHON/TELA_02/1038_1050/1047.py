horarios = input().split()
hi, mi, hf, mf = int(horarios[0]), int(horarios[1]), int(horarios[2]), int(horarios[3])
i = mi + (hi * 60)
f = mf + (hf * 60)
tempo = 0
if f > i:
    tempo = f - i
else:
    tempo = (24 * 60 - i) + f
dh = tempo // 60
dm = tempo % 60
print(f"O JOGO DUROU {dh} HORA(S) E {dm} MINUTO(S)")
