m = int(input())
a = int(input())
b = int(input())
x = m - a - b
if x > a and x > b:
    print(x)
elif a > b and a > x:
    print(a)
else:
    print(b)
