p = input().split()
x = float(p[0])
y = float(p[1])

if x == 0.0 and y == 0:
  print("Origem")
elif x == 0.0:
  print("Eixo Y")
elif y == 0.0:
  print("Eixo X")
elif x > 0.0 and y > 0.0:
  print("Q1")
elif x < 0.0 and y > 0.0:
  print("Q2")
elif x < 0.0 and y < 0.0:
  print("Q3")
else:
  print("Q4")
