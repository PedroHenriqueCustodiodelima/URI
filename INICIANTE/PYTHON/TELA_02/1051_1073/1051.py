salario = float(input())
imposto, porcentagem, a, a1, a2 = 0, 0, 0, 0, 0

if salario <= 2000:
    print("Isento")
elif salario >= 2000.01 and salario <= 3000:
    a = salario - 2000
    porcentagem = 8.0 / 100.0
    imposto = porcentagem * a
    print(f"R$ {imposto:.2f}")
elif salario >= 3000.01 and salario <= 4500:
    a = salario - 2000
    a1 = a - 1000
    porcentagem = 8.0 / 100.0
    imposto = porcentagem * (a - a1)
    porcentagem = 18.0 / 100.0
    imposto += porcentagem * a1
    print(f"R$ {imposto:.2f}")
elif salario > 4500:
    a = salario - 2000
    a1 = a - 1000
    a2 = a1 - 1500
    porcentagem = 8.0 / 100.0
    imposto = porcentagem * 1000
    porcentagem = 18.0 / 100.0
    imposto += porcentagem * 1500
    porcentagem = 28.0 / 100.0
    imposto += porcentagem * a2
    print(f"R$ {imposto:.2f}")
