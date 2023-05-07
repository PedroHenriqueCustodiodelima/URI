v = input().split(' ')
h = int(v[0])
z = int(v[1])
l = int(v[2])

if (z > h and h > l) or (z < h and h < l):
    print("huguinho")
elif (h > z and z > l) or (h < z and z < l):
    print("zezinho")
else:
    print("luisinho")
