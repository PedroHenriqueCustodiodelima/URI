a = [int(input()) for andar in range(3)]
b = []
b.append(a[0]*4 + a[1]*2)
b.append(a[0]*2 + a[2]*2)
b.append(a[1]*2 + a[2]*4)

b.sort()
print(b[0])