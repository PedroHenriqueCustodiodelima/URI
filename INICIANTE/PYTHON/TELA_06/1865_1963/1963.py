preco1, preco2 = map(float, input().split())
dif = preco2 - preco1
porcentagem = (dif * 100) / preco1
print(f"{porcentagem:.2f}%")
