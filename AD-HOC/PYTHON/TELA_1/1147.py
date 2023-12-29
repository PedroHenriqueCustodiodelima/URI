dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]
dr2 = [1, 1]
dc2 = [-1, 1]

def val(i, j):
    return 0 <= i < 8 and 0 <= j < 8

def getx(in_str):
    return int(in_str[0]) - 1

def gety(in_str):
    return ord(in_str[1]) - ord('a')

c = 1

while True:
    in_str = input().strip()
    if in_str == "0":
        break

    x = getx(in_str)
    y = gety(in_str)

    tab = [[0] * 8 for _ in range(8)]
    for _ in range(8):
        in_str = input().strip()
        tab[getx(in_str)][gety(in_str)] = 1

    ans = 0
    for i in range(8):
        if val(x + dr[i], y + dc[i]):
            flag = 0
            for j in range(2):
                if val(x + dr[i] + dr2[j], y + dc[i] + dc2[j]):
                    if tab[x + dr[i] + dr2[j]][y + dc[i] + dc2[j]]:
                        flag = 1
                        break
            if not flag:
                ans += 1

    print(f"Caso de Teste #{c}: {ans} movimento(s).")
    c += 1