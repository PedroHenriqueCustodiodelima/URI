n = int(input())
N = []
j = 0
for i in range(1000):
    N.append(j)
    print("N[{}] = {}".format(i, j))
    j += 1
    if j == n:
        j = 0
