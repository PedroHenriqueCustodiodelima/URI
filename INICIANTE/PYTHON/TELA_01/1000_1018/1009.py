nome = str(input())
salário = float(input())
vendas = float(input())
comissão = salário + (vendas * 15/100)
print("TOTAL = R$ {:.2f}".format(comissão))