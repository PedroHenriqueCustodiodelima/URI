import math

n = int(input())
x = n / math.log(n)
a = x * 1.25506
print("{:.1f} {:.1f}".format(x, a))
