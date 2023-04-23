x = int(input())
y = int(input())
menor = y
maior = x
if y > x:
    menor = x
    maior = y

a = 0
for i in range(menor, maior + 1):
    if i % 13 != 0:
        a = a + i

print(a)
