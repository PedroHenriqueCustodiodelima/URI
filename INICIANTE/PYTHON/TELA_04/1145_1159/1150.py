a = int(input())
b = int(input())

while b <= a:
    b = int(input())

c = 1
soma = a

while soma <= b:
    a += 1
    soma += a
    c += 1

print(c)
