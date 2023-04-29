while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    troco = m - n
    cedulas = 0
    while troco >= 100 and cedulas <= 2:
        troco -= 100
        cedulas += 1
    while troco >= 50 and cedulas <= 2:
        troco -= 50
        cedulas += 1
    while troco >= 20 and cedulas <= 2:
        troco -= 20
        cedulas += 1
    while troco >= 10 and cedulas <= 2:
        troco -= 10
        cedulas += 1
    while troco >= 5 and cedulas <= 2:
        troco -= 5
        cedulas += 1
    while troco >= 2 and cedulas <= 2:
        troco -= 2
        cedulas += 1
    troco2 = m - n
    if (troco == 0 and cedulas == 2) or troco2 in [4, 10, 20, 40, 100, 200]:
        print("possible")
    else:
        print("impossible")
