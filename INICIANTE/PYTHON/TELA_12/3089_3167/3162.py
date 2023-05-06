import math

def minimum(a, b):
    return a if a < b else b

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

n = int(input())
m = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    m[i] = list(map(int, input().split()))

for i in range(n):
    minimum_distance = float('inf')
    for j in range(n):
        if i != j:
            minimum_distance = minimum(minimum_distance, distance(m[i], m[j]))

    if minimum_distance < 20:
        print('A')
    elif minimum_distance < 50:
        print('M')
    else:
        print('B')
