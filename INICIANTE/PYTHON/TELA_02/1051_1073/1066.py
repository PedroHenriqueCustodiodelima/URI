numeros_pares = 0 
numeros_impares = 0
soma = 0
numeros_positivos = 0
numeros_negativos = 0

for n in range(5):
  numero = int(input())
  if (numero %2 == 0):
   numeros_pares += 1
  if (numero %2 == 1):
   numeros_impares += 1
  if numero >0:
    soma = soma + numero
    numeros_positivos = numeros_positivos + 1
  if numero <0:
    soma = soma + numero
    numeros_negativos = numeros_negativos + 1
print("{} valor(es) par(es)".format(numeros_pares))
print("{} valor(es) impar(es)".format(numeros_impares))
print("{} valor(es) positivo(s)".format(numeros_positivos))
print("{} valor(es) negativo(s)".format(numeros_negativos))