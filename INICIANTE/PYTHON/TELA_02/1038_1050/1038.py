a = [4, 4.5, 5, 2, 1.5]
n_pedido, qtde = map(int, input().split())
valor = a[n_pedido - 1] * qtde
print("Total: R$ {:0.2f}".format(valor))