numeros_pares = 0 
for n in range(5):
  numero = int(input())
  if (numero %2 == 0):
   numeros_pares += 1

print(numeros_pares,"valores pares")