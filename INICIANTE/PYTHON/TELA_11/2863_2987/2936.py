qtd_mandioca = 0
grama_ser = [300, 1500, 600, 1000, 150, 225]
for x in range(5):
    qtd_mandioca += int(input()) * grama_ser[x]
print(qtd_mandioca + grama_ser[5])
