n = int(input())
cont = 0
for i in range(n):
    cont += 6.0
    cont = 1.0 / cont
cont += 3.0
print("{:.10f}".format(cont))
