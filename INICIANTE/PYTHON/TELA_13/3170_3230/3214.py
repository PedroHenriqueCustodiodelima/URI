r = 0
resto = 0
v = input().split(' ')
e = int(v[0])
f = int(v[1])
c = int(v[2])
soma = e + f

while soma // c > 0:
    r += soma // c
    resto = soma % c
    soma = resto + soma // c

print(r)