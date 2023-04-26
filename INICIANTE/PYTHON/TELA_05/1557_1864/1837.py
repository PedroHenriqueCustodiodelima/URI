import math

v = input().split()
a = int(v[0])
b = int(v[1])
r = a % b
if r < 0:
    r += abs(b)
q = (a - r) / b
print(f"{math.floor(q)} {r}")
