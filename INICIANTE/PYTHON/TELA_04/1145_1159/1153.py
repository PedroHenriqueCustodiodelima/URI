i = 0
c = 0
vetor = [0] * 13
fatorial = 0
n = int(input())
while n > 13:
    n = int(input())

for c in range(n, 0, -1):
    if i == 0:
        i = 1
        fatorial = c
    else:
        fatorial *= c

print(fatorial)
