entrada1 = input().split(' ')
a = int(entrada1[1])
entrada2 = input().split(' ')
b = int(entrada2[0])
c = int(entrada2[2])
d = int(entrada2[4])
entrada3 = input().split(' ')
a1 = int(entrada3[1])
entrada4 = input().split(' ')
b1 = int(entrada4[0])
c1 = int(entrada4[2])
d1 = int(entrada4[4])

inicio = (a - 1) * 24 * 60 * 60 + b * 60 * 60 + c * 60 + d
fim = (a1 - 1) * 24 * 60 * 60 + b1 * 60 * 60 + c1 * 60 + d1
duracao = fim - inicio

w = duracao // (24 * 60 * 60)
resto = duracao % (24 * 60 * 60)
x = resto // (60 * 60)
resto = resto % (60 * 60)
y = resto // 60
z = resto % 60

print(f"{w} dia(s)")
print(f"{x} hora(s)")
print(f"{y} minuto(s)")
print(f"{z} segundo(s)")