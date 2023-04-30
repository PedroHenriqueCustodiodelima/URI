while True:
    try:
        line = input()
    except:
        break
    l = line.split()
    n = int(l[0])
    x = int(l[1])
    p = 0
    for i in range(n):
        c = input().split()
        if c[0] == str(x) and c[1] == "0":
            p += 1
    print(p)
