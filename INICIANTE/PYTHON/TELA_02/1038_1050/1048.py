salario = float(input())

if salario <= 400.0:
    percentual = 15.0
elif salario <= 800.0:
    percentual = 12.0
elif salario <= 1200.0:
    percentual = 10.0
elif salario <= 2000.0:
    percentual = 7.0
else:
    percentual = 4.0

reajuste = salario * percentual / 100.0
novo_salario = salario + reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {percentual:.0f} %")
