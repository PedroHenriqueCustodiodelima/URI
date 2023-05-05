n = int(input())

casa_comprado = 0
casa_sobrando = 0
trab_comprado = 0
trab_sobrando = 0

for i in range(n):
    ir_pro_trabalho, ir_pra_casa = input().split()

    if ir_pro_trabalho.lower() == 'chuva' and casa_sobrando == 0:
        casa_comprado += 1
        trab_sobrando += 1
    elif ir_pro_trabalho.lower() == 'chuva' and casa_sobrando > 0:
        trab_sobrando += 1
        casa_sobrando -= 1

    if ir_pra_casa.lower() == 'chuva' and trab_sobrando == 0:
        trab_comprado += 1
        casa_sobrando += 1
    elif ir_pra_casa.lower() == 'chuva' and trab_sobrando > 0:
        casa_sobrando += 1
        trab_sobrando -= 1

print(casa_comprado, trab_comprado)
