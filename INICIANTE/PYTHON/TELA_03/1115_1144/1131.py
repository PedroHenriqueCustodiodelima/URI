vitorias_inter = 0
vitorias_gremio = 0
empates = 0
novo_grenal = 1
while novo_grenal == 1:
    valores = input().split()
    gols_inter = int(valores[0])
    gols_gremio = int(valores[1])
    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_gremio > gols_inter:
        vitorias_gremio += 1
    else:
        empates += 1
    print("Novo grenal (1-sim 2-nao)")
    novo_grenal = int(input())
total = vitorias_gremio + vitorias_inter + empates
print(f"{total} grenais")
print(f"Inter:{vitorias_inter}")
print(f"Gremio:{vitorias_gremio}")
print(f"Empates:{empates}")
if vitorias_inter > vitorias_gremio:
    print("Inter venceu mais")
elif vitorias_gremio > vitorias_inter:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")
