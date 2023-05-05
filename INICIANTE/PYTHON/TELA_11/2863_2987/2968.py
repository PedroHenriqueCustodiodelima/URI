import math
entrada = input()
valores = entrada.split()
total_de_placas = int(valores[0]) * int(valores[1])
result = []
for i in range(1, 10):
  percentual = i / 10
  qtd_placas = total_de_placas * percentual
  qtd_placas_str = str(math.ceil(qtd_placas))
  result.append(qtd_placas_str)
result_str = " ".join(result)
print(result_str)