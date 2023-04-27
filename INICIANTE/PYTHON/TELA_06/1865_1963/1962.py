n = int(input())

for i in range(n):
    anos = int(input())
    if anos >= 2015:
        anos = anos - 2014
        print(anos, "A.C.")
    else:
        anos = 2015 - anos
        print(anos, "D.C.")
