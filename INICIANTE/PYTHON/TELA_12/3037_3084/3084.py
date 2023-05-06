try:
    while True:
        a, b = map(int, input().split())
        print("{:02d}:{:02d}".format(a // 30, b // 6))
except EOFError:
    pass
