hi, hf = map(int, input().split())

if hf > hi:
    dj = hf - hi
    print(f"O JOGO DUROU {dj} HORA(S)")
else:
    dj = (24 - hi) + hf
    print(f"O JOGO DUROU {dj} HORA(S)")
