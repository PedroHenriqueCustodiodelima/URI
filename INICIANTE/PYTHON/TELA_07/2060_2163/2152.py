n = int(input())

for i in range(n):
    v = input().split()
    h = int(v[0])
    m = int(v[1])
    o = int(v[2])
    print(f"{h:02d}:{m:02d} - A porta {'abriu!' if o == 1 else 'fechou!'}")
