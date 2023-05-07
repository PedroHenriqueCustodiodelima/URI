c = int(input().strip())
boardSize = c * c
a = (boardSize % 2) + (boardSize // 2)
b = boardSize // 2
print("{0} casas brancas e {1} casas pretas".format(a, b))
