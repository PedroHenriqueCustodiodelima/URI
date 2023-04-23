import math

x = float(input())
n = [x]

for i in range(1, 100):
    n.append(n[i-1]/2)

for j in range(100):
    print("N[{}] = {:.4f}".format(j, round(n[j], 4)))
