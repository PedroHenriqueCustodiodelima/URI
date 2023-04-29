n = int(input())
v = input().split()
r = [int(v[i]) for i in range(n)]
queda = 0
for i in range(1, n):
    if r[i] < r[i-1] and queda == 0:
        queda = i + 1
print(queda)
