cont = 0
v1 = input().split()
x = int(v1[0])
p = int(v1[1])
r = x

while cont < p:
  a = input()
  if a[0] == 'f':
    r += 1
  else:
    r -= 1
  cont += 1

print(r)
