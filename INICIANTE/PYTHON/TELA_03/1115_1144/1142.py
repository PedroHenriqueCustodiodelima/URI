n = int(input())
p1 = 1
for i in range(1, n+1):
    p2 = p1 + 1
    p3 = p1 + 2
    print(p1, p2, p3, "PUM")
    p1 += 4
