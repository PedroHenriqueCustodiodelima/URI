n = int(input())
for i in range(10000):
    resto = i % n
    if resto == 2:
        print(i)
