import sys

ans = 0
t = 0

for line in sys.stdin:
    try:
        m = float(input())
        ans += m
        t += 1
    except EOFError:
        break

if t > 0:
    print("{:.1f}".format(ans / t))
