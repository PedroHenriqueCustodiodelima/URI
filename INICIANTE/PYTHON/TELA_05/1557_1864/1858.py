menor = 21
posMenor = 0
n = int(input())
v = input().split()
for i in range(len(v)):
  t = int(v[i])
  if menor > t:
    menor = t
    posMenor = i + 1
print(posMenor)
