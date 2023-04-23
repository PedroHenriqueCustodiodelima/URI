n1 = input().split()
a = int(n1[0])
b = int(n1[1])
c = int(n1[2])
d = int(n1[3])
if b > c and d > a and c + d > a + b and c >= 0 and d >= 0:
  print("Valores aceitos")
else:
  print("Valores nao aceitos")