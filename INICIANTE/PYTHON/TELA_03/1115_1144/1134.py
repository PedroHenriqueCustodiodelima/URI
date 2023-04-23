alcool = 0
gasolina = 0
diesel = 0

tipo = int(input())

while tipo != 4:
    if tipo == 1:
        alcool += 1
    elif tipo == 2:
        gasolina += 1
    elif tipo == 3:
        diesel += 1
    tipo = int(input())

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
