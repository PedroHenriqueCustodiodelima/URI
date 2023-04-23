a = int(input())
b = int(input())

if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a

for c in range(menor+1, maior):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
